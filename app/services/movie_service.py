from sqlmodel import Session

from api.dependencies import Session_Dep
from db.models.movies_model import Movie
from db.schema.movies_schema import MovieCreate

def create_movie_service(movie:Movie, session:Session_Dep) -> Movie:
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie
