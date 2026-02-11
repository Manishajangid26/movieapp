from sqlmodel import SQLModel , Field



class Movies(SQLModel , table = True):
    id:int = Field(primary_key = True, nullable=False)
    name: str
    release_date: str
    cast: str
    rating: float
    description: str


class Post(SQLModel ):
    name: str
    release_date: str
    cast: str
    rating: float
    description: str
    