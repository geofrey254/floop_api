from typing import Annotated
from fastapi import FastAPI, Depends
from sqlmodel import Field, SQLModel, create_enginem select

class Movies(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)