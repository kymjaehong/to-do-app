from pydantic import BaseModel
from datetime import datetime


class ToDoBase(BaseModel):
    pass


class ToDoCreate(ToDoBase):
    content: str


class ToDoSchema(BaseModel):
    id: int
    content: str
    is_complete: bool
    created: datetime
    # created_at: datetime
    # modified_at: datetime

    class Config:
        orm_mode = True
