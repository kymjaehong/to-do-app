from application.service.users import UserService
from application.service.todo import ToDoService
from domain.todo import ToDo


class GetToDoByUserUsecase:
    def __init__(self):
        self._user_service = UserService()
        self._todo_service = ToDoService()

    def execute(self, user_id: int) -> list[ToDo]:
        user = self._user_service.get_user(user_id=user_id)
        return self._todo_service.get_todo_list_by_user(user=user)
