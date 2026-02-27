from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from src import get_db_seccion
from src.models import Movies
from pydantic import BaseModel


class MovieCreate(BaseModel):
    name: str
    release_date: str
    cast: str
    rating: float
    description: str


movie_router = APIRouter()



@movie_router.post("/create_movie")
def create_movie(movie: MovieCreate, db: Session = Depends(get_db_seccion)):

    new_movie = Movies(
        name=movie.name,
        release_date=movie.release_date,
        cast=movie.cast,
        rating=movie.rating,
        description=movie.description
    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie


@movie_router.get("/show_movie")
def get_movies(db: Session = Depends(get_db_seccion)):

    statement = select(Movies)
    movies = db.exec(statement).all()

    return movies
