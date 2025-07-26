from pydantic import BaseModel

class CreateCustomerSchema(BaseModel):
    name: str
    last_name: str
    email: str
    document_number: str
    address: str

class CreateSaleDetailSchema(BaseModel):
    quantity: int
    price: float
    subtotal: float
    product_id: int

class CreateSaleSchema(BaseModel):
    total: float
    customer: CreateCustomerSchema
    products: list[CreateSaleDetailSchema]