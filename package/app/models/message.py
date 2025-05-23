from pydantic import BaseModel, EmailStr

class MessageSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str | None
    message: str
    budget: str | None