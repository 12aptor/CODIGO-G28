from pydantic import BaseModel

class CreateRoleSchema(BaseModel):
    name: str