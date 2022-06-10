from sqlalchemy import Integer
from sqlmodel import SQLModel, Field, Relationship, select, join, Session,ForeignKey,Column

from database import engine

session = Session(bind=engine)

from typing import Optional, List


# from sqlmodel.orm import session


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
    # user_id = int = Field(sa_column=Column(Integer, ForeignKey("hero.id", ondelete="CASCADE")))
    user_id: int = Field(default=None, foreign_key="user_data.id")
    user: Optional[User] = Relationship(back_populates="cars", sa_relationship_kwargs={"cascade":"all, delete"})

#
# car = Car()
# user = User()
# car.user = user
# stmt = select(Car, User).select_from(join(Car, User))
# data = session.exec(stmt).all()
# print(data)
