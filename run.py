from src import app
from src.home import home_router

app.include_router(home_router)