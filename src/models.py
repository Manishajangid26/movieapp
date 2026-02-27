from sqlmodel import SQLModel , Field
from typing import Optional



class Movies(SQLModel , table = True):
    id:Optional[int] = Field(primary_key = True, nullable=False)
    name: str
    release_date: str
    cast: str
    rating: float
    description: str


    