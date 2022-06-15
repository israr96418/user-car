from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = "user_data"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    phone: Optional[str]
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())

    cars: List["Car"] = Relationship(back_populates="user")


class Car(SQLModel, table=True):
    __tablename__ = "car_data"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    color: str

    user_id: Optional[int] = Field(default=None, foreign_key="user_data.id")
    users: Optional[User] = Relationship(back_populates="cars")
