import datetime
from pydantic import BaseModel
from typing import Optional

class MovieBase(BaseModel):
    title:str
    description:str
    release_year:int
    rating:Optional[float] = None
    language:str
    poster_url:Optional[str] = None
    is_published:bool = False


class MovieCreate(MovieBase):
    pass

class MovieRead(MovieBase):
    id:int
    created_at:datetime.datetime
    updated_at:datetime.datetime