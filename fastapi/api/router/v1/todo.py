from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db.database import db_get

from domain.todo.schemas import ToDoCreate, ToDo
import api.service.todo

router = APIRouter()


@router.get("/{user_id}", response_model=list[ToDo])
def get_todos(user_id: int, db: Session = Depends(db_get)) -> ToDo:
    to_dos = api.service.todo.get_todos(db=db, user_id=user_id)
    return to_dos


@router.post("/{user_id}", response_model=ToDo)
def create_todo(user_id: int, to_do: ToDoCreate, db: Session = Depends(db_get)) -> ToDo:
    return api.service.todo.create_todo(user_id=user_id, to_do=to_do, db=db)


@router.get("/{user_id}/search", response_model=list[ToDo])
def search_todos(user_id: int, keyword: str, db: Session = Depends(db_get)):
    to_dos = api.service.todo.search_todos(user_id=user_id, keyword=keyword, db=db)
    return to_dos


@router.patch("/complete/{to_do_id}")
def update_todo(to_do_id: int, db: Session = Depends(db_get)):
    api.service.todo.update_todo(to_do_id=to_do_id, db=db)
