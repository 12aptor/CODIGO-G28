from pydantic import BaseModel, EmailStr

class RegisterSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str
    role_id: int