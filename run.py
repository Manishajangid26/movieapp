from src import app
# from src.home import home_router
from src.movie import movie_router

# app.include_router(home_router)
app.include_router(movie_router)