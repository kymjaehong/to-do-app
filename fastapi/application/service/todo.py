from adapter.todo_repository import ToDoRepository
from domain.todo import ToDo
from domain.users import User


class ToDoService:
    def __init__(self):
        self._to_do_repository = ToDoRepository()

    def get_todo_list_by_user(self, user: User) -> list[ToDo]:
        return self._to_do_repository.find_all_by_user(user=user)

    def search_todo_list(self, user: User, keyword: str) -> list[ToDo]:
        return self._to_do_repository.find_all_by_user_and_keyword(
            user=user, keyword=keyword
        )

    def create_todo(self, to_do: ToDo) -> ToDo:
        return self._to_do_repository.save(to_do=to_do)

    def update_todo(self, to_do_id: int) -> ToDo:
        to_do = self._to_do_repository.find_by_id(to_do_id=to_do_id)
        to_do.update_is_complete()
        return self._to_do_repository.save(to_do=to_do)
