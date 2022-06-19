from fastapi import APIRouter, Depends
from sqlmodel import Session

# from Router import user
from app import schemas, crud
from app.database import get_db
from app.models import Car

router = APIRouter(
    prefix="/car",
    tags=['Car']
)


@router.post("/", response_model=Car)
def add_car(car_data: schemas.CarsSchema, db: Session = Depends(get_db)):
    db_user = crud.add_car(db, car_data)
    return db_user


@router.get("/")
def get_user(car_id:int, db: Session = Depends(get_db)):
    db_user = crud.get_car_by_id(db, car_id)
    return db_user