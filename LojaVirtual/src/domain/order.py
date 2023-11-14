from pydantic import BaseModel,Field

class OrderStatus(BaseModel):
    name: str

class OrderItem(BaseModel):
    product_id: int
    price: float
    quantity: int

class Order(BaseModel):
    status: list[OrderStatus] = Field(default = [])
    items: list[OrderItem] = Field(default = [])