from datetime import datetime

from app.domain.user import User
from app.api.v1.request.todo_request import ToDoCommand

"""
N:1 테이블의 경우,
테이블에 1에 대한 PK를 FK로 가지고 있기 때문에, 이는 필드로 정한다.
lazy loading을 위한 elationship에 필드를 선언해둔다.
"""


class ToDo:
    def __init__(
        self, id: int, content: str, is_complete: bool, created: datetime, user: User
    ):
        self.id = id
        self.content = content
        self.is_complete = is_complete
        self.created = created
        self.user_id = user.id
        self.user = user  # relationship

    @classmethod
    def _validate(cls) -> bool:
        return True

    @classmethod
    def create(cls, command: ToDoCommand, created: datetime, user: User) -> "ToDo":
        if not cls._validate():
            raise Exception("validate Exception")
        return cls(
            id=0, content=command.content, is_complete=False, created=created, user=user
        )

    def update_is_complete(self):
        self.is_complete = not self.is_complete
