from sqlmodel import SQLModel, Field, Relationship

from typing import Optional, List


class UserInSchema(SQLModel):
    name: str
    phone: str


class User(UserInSchema, table=True):
    __tablename__ = "user_data"
    id: Optional[int] = Field(default=None, primary_key=True)
    cars: List["Car"] = Relationship(back_populates="user")


class CarInSchema(SQLModel):
    name: str
    color: str


class Car(CarInSchema, table=True):
    __tablename__ = "car_data"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user_data.id")
    user: Optional[User] = Relationship(back_populates="cars")


object = Car()
# print(object.user.json())