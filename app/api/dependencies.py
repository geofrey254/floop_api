from db.session import get_session
from typing import Annotated
from sqlmodel import Session
from fastapi import Depends

Session_Dep = Annotated[Session, Depends(get_session)]