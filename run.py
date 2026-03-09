from src import app

from src.movie import movie_router


app.include_router(movie_router)