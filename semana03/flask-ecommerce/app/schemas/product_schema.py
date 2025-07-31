from pydantic import BaseModel
from typing import Optional

class CreateProductSchema(BaseModel):
    name: str
    description: str
    brand: str
    size: str
    price: float
    stock: int
    category_id: int

class UpdateProductSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    brand: Optional[str] = None
    size: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category_id: Optional[int] = None
