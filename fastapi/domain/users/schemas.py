from pydantic import BaseModel
from domain.todo import schemas


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    phone_number: str
    name: str


class User(UserBase):
    id: int
    phone_number: str
    name: str
    to_dos: list[schemas.ToDo] = []

    class Config:
        orm_mode = True
