from fastapi import FastAPI

from app.Router import user, car
app = FastAPI()

app.include_router(user.router)
app.include_router(car.router)