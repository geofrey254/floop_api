import datetime
from typing import Annotated
from fastapi import FastAPI, Depends
from sqlmodel import Field, SQLModel, create_engine, select

class Movie(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str = Field(index=True)
    release_year: datetime = Field(index=True)
    duration_minutes:int
    rating:float | None = Field(ge=0, le=10)
    language:str
    is_published:bool = Field(default=False)
    created_at:datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
