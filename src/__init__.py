from fastapi import FastAPI
from sqlmodel import SQLModel , create_engine , Session
from src.models import Movies


app = FastAPI()

database_file = "sqlite:///movie.db"

engine = create_engine(database_file)
SQLModel.metadata.create_all(engine)