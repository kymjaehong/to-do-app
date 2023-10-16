from pydantic import BaseModel
from datetime import datetime

from app.domain.todo.todo_schema import ToDoSchema


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    phone_number: str
    name: str


class UserSchema(UserBase):
    id: int
    phone_number: str
    name: str
    # created_at: datetime
    # modified_at: datetime
    to_dos: list[ToDoSchema] = list()

    class Config:
        orm_mode = True
