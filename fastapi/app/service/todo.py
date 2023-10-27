from app.adapter.todo import AbstractToDoRepostiroy
from app.domain.todo import ToDo
from app.domain.user import User


class ToDoService:
    def __init__(self, todo_repository: AbstractToDoRepostiroy):
        self._to_do_repository = todo_repository

    async def get_todo_list_by_user(self, user: User) -> list[ToDo]:
        return await self._to_do_repository.find_all_by_user(user=user)

    async def get_todo_list_by_user_and_is_completed(
        self, user: User, is_completed: bool | None
    ) -> list[ToDo]:
        return await self._to_do_repository.find_all_by_user_and_is_completed(
            user=user, is_completed=is_completed
        )

    async def search_todo_list(self, user: User, keyword: str) -> list[ToDo]:
        return await self._to_do_repository.find_all_by_user_and_keyword(
            user=user, keyword=keyword
        )

    async def create_todo(self, to_do: ToDo) -> ToDo:
        return await self._to_do_repository.save(to_do=to_do)

    async def update_todo(self, to_do_id: int) -> ToDo:
        to_do = await self._to_do_repository.find_by_id(to_do_id=to_do_id)
        to_do.update_is_complete()
        return await self._to_do_repository.save(to_do=to_do)
