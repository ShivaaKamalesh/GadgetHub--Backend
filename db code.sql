create database GadgetHub;

use GadgetHub;

create table product(
	product_id int auto_increment primary key,
    name varchar(30),
    category varchar(30),
    price decimal(10,3),
   
    stock int,
    created_at timestamp default current_timestamp
);

drop table product;

select * from product;

show tables;

INSERT INTO product (name, category, price, stock) VALUES
('iPhone 14', 'Mobile', 69999.000, 15),
('Samsung Galaxy S23', 'Mobile', 74999.000, 20),
('Redmi Note 12', 'Mobile', 17999.000, 30),
('Realme Narzo 60', 'Mobile', 18999.000, 25),
('OnePlus Nord CE 3', 'Mobile', 24999.000, 18),

('Dell Inspiron 15', 'Laptop', 55999.000, 10),
('HP Pavilion 14', 'Laptop', 62999.000, 8),
('Lenovo IdeaPad Slim 3', 'Laptop', 48999.000, 12),
('Asus VivoBook 15', 'Laptop', 52999.000, 9),
('MacBook Air M1', 'Laptop', 82999.000, 6),

('Boat Rockerz 450', 'Headphones', 1499.000, 40),
('Sony WH-1000XM4', 'Headphones', 24999.000, 7),
('JBL Tune 760NC', 'Headphones', 7999.000, 14),
('Noise Cancelling Buds', 'Headphones', 3999.000, 22),
('Apple AirPods Pro', 'Headphones', 24999.000, 10),

('Logitech Wireless Mouse', 'Accessories', 999.000, 50),
('HP USB Keyboard', 'Accessories', 799.000, 45),
('Dell 24 Inch Monitor', 'Accessories', 13999.000, 11),
('Samsung SSD 1TB', 'Accessories', 7499.000, 16),
('SanDisk Pendrive 64GB', 'Accessories', 699.000, 60),

('Apple iPad 10th Gen', 'Tablet', 44999.000, 13),
('Samsung Galaxy Tab S8', 'Tablet', 58999.000, 9),
('Lenovo Tab M10', 'Tablet', 15999.000, 20),
('Realme Pad', 'Tablet', 13999.000, 18),
('Mi Pad 5', 'Tablet', 26999.000, 12),

('Canon EOS 1500D', 'Camera', 38999.000, 7),
('Nikon D3500', 'Camera', 41999.000, 6),
('Sony Alpha ILCE-6400', 'Camera', 79999.000, 4),
('GoPro Hero 11', 'Camera', 49999.000, 5),
('DJI Mini 2 Drone', 'Camera', 35999.000, 3);

Select * from product;

DROP table product;

