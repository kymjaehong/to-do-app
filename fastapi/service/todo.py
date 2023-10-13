from sqlalchemy.orm import Session

from models.todo import ToDo
from schemas.todo import ToDoCreate


def get_todos(db: Session, user_id: int) -> list[ToDo]:
    return db.query(ToDo).filter(ToDo.user_id == user_id).all()


def create_todo(db: Session, to_do: ToDoCreate, user_id: int) -> ToDo:
    db_todo = ToDo(content=to_do.content, user_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def search_todos(db: Session, user_id: int, keyword: str) -> list[ToDo]:
    return (
        db.query(ToDo)
        .filter(ToDo.user_id == user_id, ToDo.content.contains(keyword))
        .all()
    )


def update_todo(db: Session, to_do_id: int):
    db_todo = db.query(ToDo).filter(ToDo.id == to_do_id).first()
    if db_todo is None:
        return None

    db_todo.is_complete = not db_todo.is_complete

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
