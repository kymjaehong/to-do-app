from router.v1.schemas.users import UserCreate
from adapter.user_repository import UserRepository
from domain.users import User


class UserService:
    def __init__(self):
        self._user_repository = UserRepository()

    def get_user(self, user_id: int) -> User:
        return self._user_repository.find_by_id(user_id=user_id)

    def create_user(self, user: UserCreate) -> User:
        db_user = User(**user.model_dump())
        pass
