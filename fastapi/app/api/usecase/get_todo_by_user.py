from app.service.user import UserService
from app.service.todo import ToDoService
from app.domain.todo import ToDo


class GetToDoByUserUsecase:
    def __init__(self, user_service: UserService, todo_service: ToDoService):
        self._user_service = user_service
        self._todo_service = todo_service

    async def execute(self, user_id: int) -> list[ToDo]:
        user = await self._user_service.get_user(user_id=user_id)
        print(f"usecase user: {user}")
        return await self._todo_service.get_todo_list_by_user(user=user)
