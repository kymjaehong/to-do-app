from app.api.v1.request.user_request import UserCommand

"""
1:N 테이블의 경우
eager loading을 위한 relationship 필드를 설정해둔다.
"""


class User:
    def __init__(self, id: int, phone_number: str, name: str):
        self.id = id
        self.phone_number = phone_number
        self.name = name
        self.todo_list = list()  # relationship

    @classmethod
    def _validate(cls) -> bool:
        return True

    @classmethod
    def create(cls, command: UserCommand) -> "User":
        if not cls._validate():
            raise Exception("validate Exception")
        return cls(id=0, phone_number=command.phone_number, name=command.name)
