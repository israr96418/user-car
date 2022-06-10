from fastapi import FastAPI

import Router.user
from database import engine
from Router import user, car
app = FastAPI()

app.include_router(user.router)
app.include_router(car.router)

""" copy from sqlmodel website"""
#
# from sqlmodel import SQLModel, Field, Relationship, create_engine, select, Session, join
# from typing import Optional, List
#
# engine = create_engine("sqlite://")
#
#
# class UserInSchema(SQLModel):
#     name: str
#     phone: str
#
#
# class User(UserInSchema, table=True):
#     __tablename__ = "user_data"  # type: ignore
#     id: Optional[int] = Field(default=None, primary_key=True)
#     cars: List["Car"] = Relationship(back_populates="user")
#
#
# class CarInSchema(SQLModel):
#     name: str
#     color: str
#
#
# class Car(CarInSchema, table=True):
#     __tablename__ = "car_data"  # type: ignore
#     id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: int = Field(default=None, foreign_key="user_data.id")
#     user: Optional[User] = Relationship(back_populates="cars")
#
#
# stmt = select(Car, User).select_from(join(Car, User))
#
# with Session(engine) as session:
#     SQLModel.metadata.create_all(session.bind)
#
#     user = User(name="israr", phone="03359696418")
#     car = Car(name="toyota", color="white")
#     car.user = user
#     session.add(user)
#     session.add(car)
#     session.commit()
#
#     data = session.exec(stmt).all()
#
# print(data)
# data=[(Car(name='car', user_id=1, id=1, color='color'), User(phone='phone', name='user', id=1))]