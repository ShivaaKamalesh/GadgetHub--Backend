# from fastapi import FastAPI,HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from database import get_connection
# from schemas import ProductCreate,ProductUpdate

# app=FastAPI()

# # CORS for connection
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # add product
# @app.post("/products")
# def add_products(product:ProductCreate):
#     try:
#         conn=get_connection()
#         cursor=conn.cursor()

#         query="""
#             Insert into product (name,category,price,stock) VALUES(%s,%s,%s,%s)
#         """
#         values=(
#             product.name,
#             product.category,
#             product.price,
#             product.stock
#         )

#         cursor.execute(query,values)
#         conn.commit()

#         return{
#             "message":"Product added",
#             "product_id":cursor.lastrowid
#         }
    
#     except Exception as e:
#         raise HTTPException(status_code=404,detail=str(e))
#     finally:
#         cursor.close()
#         conn.close()


# # update stock
# @app.put("/products/{product_id}/stock")
# def update_product_stock(product_id:int,product:ProductUpdate):
#     try:
#         conn=get_connection()
#         cursor=conn.cursor()
        
#         cursor.execute(
#             "select stock from product where product_id=%s",
#             (product_id,)
#         )
#         result=cursor.fetchone()

#         if not result:
#             raise HTTPException(status_code=500,detail="Product not found")
        
#         if product.stock<0:
#             raise HTTPException(status_code=400,detail="Stock cannot be less than 0")
        
#         cursor.execute(
#             "update product set stock=%s where product_id=%s",
#             (product.stock,product_id)
#         )
#         conn.commit()
#         return {
#             "message": "Stock updated successfully",
#             "product_id": product_id,
#             "new_stock": product.stock
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500,detail=str(e))
#     finally:
#         cursor.close()
#         conn.close()
    
# # low stock
# @app.get("products/low-stock")
# def get_low_stock(threshold:int=5):
#     try:
#         conn=get_connection()
#         cursor=conn.cursor()

#         cursor.execut(
#             "Select * from products where stock<%s"
#             (threshold,)
#             )
#         products=cursor.fetchall()

#         return{
#             "message":"Prducts taken that are below threshold value",
#             "low_stock_product":products
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500,detail=str(e))
#     finally:
#         cursor.close()
#         conn.close()

# # filter
# @app.get("/products/filter")
# def filter_products(category:str=None,min_price:float=None,max_price:float=None):
#     try:
#         conn=get_connection()
#         cursor=conn.cursor()

#         query="Select * from products where 1=1"
#         values=[]

#         if category:
#             query+="AND category=%s"
#             values.append(category)

#         if min_price is not None:
#             query += " AND price >= %s"
#             values.append(min_price)

#         if max_price is not None:
#             query += " AND price <= %s"
#             values.append(max_price)

#         cursor.execute(query,values)
#         products=cursor.fetchall()

#         return{
#             "count":len(products),
#             "products":products
#         }
    
#     except Exception as e:
#         raise HTTPException(status_code=500,detail=str(e))
    
#     finally:
#         cursor.close()
#         conn.close()

# # filter by category
# @app.get("/products/filter/category")
# def filter_by_category(category: str):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "SELECT * FROM products WHERE category = %s",
#             (category,)
#         )
#         products = cursor.fetchall()

#         return {
#             "count": len(products),
#             "products": products
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#     finally:
#         cursor.close()
#         conn.close()

# # filter by name
# @app.get("/products/filter/name")
# def filter_by_name(name: str):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "SELECT * FROM products WHERE name LIKE %s",
#             (f"%{name}%",)
#         )
#         products = cursor.fetchall()

#         return {
#             "count": len(products),
#             "products": products
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#     finally:
#         cursor.close()
#         conn.close()
        
# # dashboard

# @app.get("/dashboard/summary")
# def dashboard_summary(threshold:int=5):
#     try:
#         conn=get_connection()
#         cursor=conn.cursor()

#         cursor.execute("Select count(*) as total from product")
#         total_product=cursor.fetchone()["total"]

#         cursor.execute("Select count(*) as low from products where stock<%s",(threshold,))
#         low_stock=cursor.fetchone()["low"]

#         cursor.execute("Select count(distinct category) as categories from products")
#         category=cursor.fetchone()["categories"]

#         return{
#             "total_product":total_product,
#             "low_stock":low_stock,
#             "categories":category
#         }
    
#     except Exception as e:
#         raise HTTPException(status_code=500,detail=str(e))
    
#     finally:
#         conn.close()
#         cursor.close()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection
from schemas import ProductCreate, ProductUpdate

app = FastAPI()

# ===== CORS =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===== ADD PRODUCT =====
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



# ===== UPDATE STOCK =====
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



# ===== LOW STOCK =====
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



# ===== FILTER PRODUCTS =====
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



# ===== DASHBOARD =====
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