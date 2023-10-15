from domain.todo import ToDo
from sqlalchemy import DateTime
from router.v1.schemas.todo import ToDoCreate
from application.service.todo import ToDoService
from application.service.users import UserService


class RegisterToDoUsecase(object):
    def __init__(self):
        self._todo_service = ToDoService()
        self._user_service = UserService()

    def execute(
        self, user_id: int, to_do_create: ToDoCreate, created_now: DateTime
    ) -> int:
        user = self._user_service.get_user(user_id=user_id)
        new_todo = ToDo.create(
            content=to_do_create.content, created=created_now, user_id=user.id
        )
        return self._todo_service.create_todo(new_todo)
