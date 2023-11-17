from app.domain.todo import ToDo
from app.api.v1.request.todo_request import ToDoCommand
from app.service.user import UserService
from app.service.todo import ToDoService


class RegisterToDoUsecase(object):
    def __init__(self, user_service: UserService, todo_service: ToDoService):
        self._user_service = user_service
        self._todo_service = todo_service

    async def execute(self, user_id: int, command: ToDoCommand):
        user = await self._user_service.get_user(user_id=user_id)
        new_todo = ToDo(**command.__dict__, user=user)
        return await self._todo_service.create_todo(new_todo)
