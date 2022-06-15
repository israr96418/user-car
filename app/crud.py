from sqlmodel import select
from .database import Session
from . import models, schemas


def get_car_by_id(db: Session, car_id: int):
    query = select(models.Car).where(models.Car.id == car_id)
    return db.exec(query).first()


def get_user_by_id(db: Session, user_id: int):
    query = select(models.User).where(models.Car.id == user_id)
    return db.exec(query).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    query = select(models.User).offset(skip).limit(limit)
    return db.exec(query).all()


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    query = select(models.Car).offset(skip).limit(limit)
    return db.exec(query).all()


def add_user(db: Session, user: schemas.UserSchema):
    db_user = models.User(
        name=user.name,
        phone=user.phone,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def add_car(db: Session, car: schemas.CarsSchema):
    db_car = models.Car(
        name=car.name,
        color=car.color,
        user_id=car.user_id,
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car
