from pydantic import BaseModel
from router.v1.schemas.todo import ToDo


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    phone_number: str
    name: str


class User(UserBase):
    id: int
    phone_number: str
    name: str
    to_dos: list[ToDo] = []

    class Config:
        orm_mode = True
