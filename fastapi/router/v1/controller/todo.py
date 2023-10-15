from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from core.database.database import db_get, db_session
from router.v1.schemas.todo import ToDoCreate
from router.v1.schemas.todo import ToDo
from application.service.todo import ToDoService
from application.usecase.get_todo_by_user import GetToDoByUserUsecase
from application.usecase.register_todo import RegisterToDoUsecase
from application.usecase.get_todo_by_cond import GetToDoByCondUsecase

router = APIRouter()

to_do_service = ToDoService()
get_todo_by_user_usecase = GetToDoByUserUsecase()
register_todo_usecase = RegisterToDoUsecase()
get_todo_by_cond_usecase = GetToDoByCondUsecase()


@router.get("/{user_id}", response_model=list[ToDo])
def get_todo_list(user_id: int, db: Session = Depends(db_get)):
    db_session.set(db)
    return get_todo_by_user_usecase.execute(user_id=user_id)


@router.get("/{user_id}/search", response_model=list[ToDo])
def search_todo_list(user_id: int, keyword: str, db: Session = Depends(db_get)):
    db_session.set(db)
    return get_todo_by_cond_usecase.execute(user_id=user_id, keyword=keyword)


@router.post("/{user_id}", response_model=ToDo)
def register_todo(
    user_id: int, to_do_create: ToDoCreate, db: Session = Depends(db_get)
) -> ToDo:
    db_session.set(db)
    created_now = func.now()
    return register_todo_usecase.execute(
        user_id=user_id, to_do_create=to_do_create, created_now=created_now
    )


@router.patch("/complete/{to_do_id}", response_model=ToDo)
def update_todo(to_do_id: int, db: Session = Depends(db_get)) -> ToDo:
    db_session.set(db)
    return to_do_service.update_todo(to_do_id=to_do_id)
