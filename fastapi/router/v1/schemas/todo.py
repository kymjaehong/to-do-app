from pydantic import BaseModel
from datetime import datetime


class ToDoBase(BaseModel):
    pass


class ToDoCreate(ToDoBase):
    content: str


class ToDo(BaseModel):
    id: int
    content: str
    is_complete: bool
    created: datetime

    class Config:
        orm_mode = True
