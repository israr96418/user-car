from fastapi import FastAPI, Depends, status, APIRouter, HTTPException
from sqlmodel import Session, select, join

# from Router import user
from database import engine
from models import Car, User

session = Session(bind=engine)

user = User()
car = Car()

router = APIRouter(
    prefix="/car",
    tags=['Car']
)


@router.post("/", response_model=Car)
def Car_data(data: Car):
    car_data = Car(**data.dict())
    print(car_data)
    session.add(car_data)
    session.commit()
    session.refresh(car_data)
    return car_data


@router.get("/")
def get():
    # stmt = select(Car, User).select_from(join(Car, User))
    stmt = session.exec(select(Car, User).join(User).where(Car.user_id == User.id)).all()
    car.user = user
    # data = session.exec(stmt).all()
    # print(data)
    return stmt


@router.delete("/{id}")
def deletedata(id: int):
    data = session.exec(select(Car).where(Car.id == id)).one_or_none()
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Car with id{id} is not found")
    else:
        session.delete(data)
        session.commit()
        return {"message": "Car has been successfully deleted"}
