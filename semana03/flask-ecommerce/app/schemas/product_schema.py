from pydantic import BaseModel

class CreateProductSchema(BaseModel):
    name: str
    description: str
    brand: str
    size: str
    price: float
    stock: int
    category_id: int
