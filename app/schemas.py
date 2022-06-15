from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    phone: Optional[str]


class CarsSchema(BaseModel):
    id: Optional[int] = None
    name: str
    color: str
    user_id: Optional[int]
