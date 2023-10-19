from datetime import datetime

from app.domain.todo import ToDo
from app.api.v1.request.todo_request import ToDoCommand
from app.service.user_service import UserService
from app.service.todo_service import ToDoService


class RegisterToDoUsecase(object):
    def __init__(self, user_service: UserService, todo_service: ToDoService):
        self._user_service = user_service
        self._todo_service = todo_service

    async def execute(self, user_id: int, command: ToDoCommand, created_now: datetime):
        user = await self._user_service.get_user(user_id=user_id)
        new_todo = ToDo.create(command=command, created=created_now, user=user)
        return await self._todo_service.create_todo(new_todo)
