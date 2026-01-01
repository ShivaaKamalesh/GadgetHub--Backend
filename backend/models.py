# to say what all the items are there

class Product:
    def __init__(self,product_id,name,category,price,discount_price,stock,created_at):
        self.product_id=product_id
        self.name=name
        self.category=category
        self.price=price
        self.discount_price=discount_price
        self.stock=stock
        self.created_at=created_at

# testing

if __name__ =="__main__":
    p=Product(1,"lap","Elec",500,440,20,"2025-01-20")

    print(p.name)
    print(p.discount_price)
        


# create table product(
# 	product_id int auto_increment primary key,
#     name varchar(30),
#     category varchar(30),
#     price decimal(10,3),
#     discount_price DECIMAL(10,3),
#     stock int,
#     created_at timestamp default current_timestamp,
#     CHECK (discount_price <= price * 0.10)
# );
