from domain.todo import ToDo
from domain.users import User
from core.database.database import session


class ToDoRepository:
    def __init__(self):
        self._db = session

    def find_by_id(self, to_do_id: int) -> ToDo:
        todo = self._db.query(ToDo).filter(ToDo.id == to_do_id).one_or_none()
        if todo is None:
            raise Exception(f"not found by id {to_do_id}")
        return todo

    def find_all_by_user(self, user: User) -> list[ToDo]:
        return self._db.query(ToDo).filter(ToDo.user == user).all()

    def save(self, to_do: ToDo) -> ToDo:
        self._db.add(to_do)
        self._db.commit()
        self._db.refresh(to_do)
        return to_do

    def find_all_by_user_and_keyword(self, user: User, keyword: str) -> list[ToDo]:
        return (
            self._db.query(ToDo)
            .filter(ToDo.user == user, ToDo.content.contains(keyword))
            .all()
        )
