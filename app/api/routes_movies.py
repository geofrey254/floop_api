from fastapi import APIRouter
from db.schema.movies_schema import MovieRead, MovieCreate
from api.dependencies import Session_Dep
from services.movie_service import create_movie_service
 
router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/", response_model=MovieRead)
def create_movie(movie:MovieCreate, session:Session_Dep):
    
    return create_movie_service(movie, session)