from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection
from schemas import ProductCreate, ProductUpdate

app = FastAPI()
# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  ADD PRODUCT 
@app.post("/products")
def add_product(product: ProductCreate):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO product (name, category, price, stock)
            VALUES (%s, %s, %s, %s)
            """,
            (product.name, product.category,
             product.price, product.stock)
        )

        conn.commit()

        return {"message": "Product added", "product_id": cursor.lastrowid}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()

# UPDATE STOCK
@app.put("/products/{product_id}/stock")
def update_product_stock(product_id: int, product: ProductUpdate):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT product_id FROM product WHERE product_id = %s",
            (product_id,)
        )

        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Product not found")

        if product.stock < 0:
            raise HTTPException(status_code=400, detail="Stock cannot be negative")

        cursor.execute(
            "UPDATE product SET stock=%s WHERE product_id=%s",
            (product.stock, product_id)
        )

        conn.commit()

        return {"message": "Stock updated"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()

#LOW STOCK 
@app.get("/products/low-stock")
def get_low_stock(threshold: int = 5):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM product WHERE stock < %s",
            (threshold,)
        )

        return {"products": cursor.fetchall()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()

#  FILTER PRODUCT
@app.get("/products/filter")
def filter_products(category: str = None, min_price: float = None, max_price: float = None):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM product WHERE 1=1"
        values = []

        if category:
            query += " AND category=%s"
            values.append(category)

        if min_price is not None:
            query += " AND price >= %s"
            values.append(min_price)

        if max_price is not None:
            query += " AND price <= %s"
            values.append(max_price)

        cursor.execute(query, values)

        products = cursor.fetchall()

        return {"products": products}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()



# DASHBOARD
@app.get("/dashboard/summary")
def dashboard_summary(threshold: int = 5):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT COUNT(*) AS total FROM product")
        total = cursor.fetchone()["total"]

        cursor.execute(
            "SELECT COUNT(*) AS low FROM product WHERE stock < %s",
            (threshold,)
        )
        low = cursor.fetchone()["low"]

        cursor.execute(
            "SELECT COUNT(DISTINCT category) AS categories FROM product"
        )
        categories = cursor.fetchone()["categories"]

        return {
            "total_products": total,
            "low_stock": low,
            "categories": categories
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()

        conn.close()
