from fastapi import status, APIRouter, HTTPException
from sqlmodel import Session, select, join

from database import engine
from models import UserInSchema, User, Car

session = Session(bind=engine)

router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def Userdata(data: UserInSchema):
    user_data = User(**data.dict())
    session.add(user_data)
    session.commit()
    session.refresh(user_data)
    return user_data


@router.get("/")
def get():
    # both work correctly
    result = session.exec(select(User, Car).join(Car)).all()
    # result = session.exec(select(User, Car).select_from(join(User, Car))).all()
    return result


@router.delete("/{id}")
def deletedata(id: int):
    data = session.exec(select(User).where(User.id == id)).first()
    if data is None:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id{id} is not found")
    else:
        session.delete(data)
        session.commit()
        return {"message": "user has been successfully deleted"}
