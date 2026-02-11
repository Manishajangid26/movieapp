from src import app
from fastapi import APIRouter

from src.data import data

home_router = APIRouter()


@home_router.get("/movie")
def movie():
    return {"msg" : "movie"}

@home_router.post("/user_dats")
def user_data(username:str,password:str ):
    return [username,password]




@home_router.post("/list_user")
def user_data( ):
    a = []
    for x in data.get("users"):
        a.append({
            "id": x.get("id"),
            "name": x.get("firstName"),
            "age": x.get("age"),
            "hair_color": x.get("hair").get("color")

        })
    return  a