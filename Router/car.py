from fastapi import FastAPI, Depends, status, APIRouter
from sqlmodel import Session, select

from database import engine
from models import Car, User

session = Session(bind=engine)

router = APIRouter(
    prefix="/car",
    tags=['Car']
)


@router.post("/", response_model=Car)
def User(data: Car):
    car_data = Car(**data.dict())
    session.add(car_data)
    session.commit()
    session.refresh(car_data)
    return car_data


@router.get("/")
def get():
    result = session.exec(select(Car)).all()
    return result
