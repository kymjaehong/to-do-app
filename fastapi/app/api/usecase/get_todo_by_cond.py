from app.service.user import UserService
from app.service.todo import ToDoService
from app.domain.todo import ToDo


class GetToDoByCondUsecase:
    def __init__(self, user_service: UserService, todo_service: ToDoService):
        self._user_service = user_service
        self._todo_service = todo_service

    async def execute(self, user_id: int, keyword: str) -> list[ToDo]:
        user = await self._user_service.get_user(user_id=user_id)
        return await self._todo_service.search_todo_list(user=user, keyword=keyword)
