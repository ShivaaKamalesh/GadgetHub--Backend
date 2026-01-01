from pydantic import BaseModel

from typing import Optional
from datetime import datetime

class ProductCreate(BaseModel):
    name:str
    category:str
    price:int
    stock:int

class ProductUpdate(BaseModel):
    stock:int

class ResponseModel(BaseModel):
    product_id:int
    name:str
    category:str
    price:int
    stock:int
    created_at:datetime