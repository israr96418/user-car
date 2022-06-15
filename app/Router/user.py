from fastapi import APIRouter, Depends
from sqlmodel import Session

from app import schemas, crud
from app.database import get_db

router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.post("/")
def add_user(user_data: schemas.UserSchema, db: Session = Depends(get_db)):
    db_user = crud.add_user(db, user_data)
    return db_user


@router.get("/")
def get_user(user_id:int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    return db_user