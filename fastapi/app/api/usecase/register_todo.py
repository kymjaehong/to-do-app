from datetime import datetime

from app.domain.todo.todo import ToDo
from app.domain.todo.todo_schema import ToDoCreate
from app.domain.users.user_service import UserService
from app.domain.todo.todo_service import ToDoService


class RegisterToDoUsecase(object):
    def __init__(self, user_service: UserService, todo_service: ToDoService):
        self._user_service = user_service
        self._todo_service = todo_service

    async def execute(
        self, user_id: int, to_do_create: ToDoCreate, created_now: datetime
    ):
        user = await self._user_service.get_user(user_id=user_id)
        new_todo = ToDo.create(
            content=to_do_create.content, created=created_now, user_id=user.id
        )
        return await self._todo_service.create_todo(new_todo)
