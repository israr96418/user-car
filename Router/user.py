from pprint import pprint

from fastapi import FastAPI, Depends, status, APIRouter
from sqlmodel import Session, select

from database import engine
from models import UserInSchema, User, Car

session = Session(bind=engine)

router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def Userdata(data: UserInSchema):
    print("data: ", data)
    user_data = User(**data.dict())
    # print("database", db)
    session.add(user_data)
    session.commit()
    session.refresh(user_data)
    return user_data


@router.get("/")
def get():
    result = session.exec(select(User,Car).join(Car).where(User.id == Car.user_id)).all()
    return result
