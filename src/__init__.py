from fastapi import FastAPI
from sqlmodel import SQLModel , create_engine , Session
from src.models import Movies
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:5173",  # Your React app's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

database_file = "sqlite:///movie.db"

engine = create_engine(database_file)
SQLModel.metadata.create_all(engine)

def get_db_seccion():
    with Session(engine) as db:
        yield db
