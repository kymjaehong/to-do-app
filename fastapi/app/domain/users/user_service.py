from app.domain.users.user_schema import UserCreate
from app.domain.users.user_repository import AbstractUserRepository
from app.domain.users.users import User


class UserService:
    def __init__(self, user_repository: AbstractUserRepository):
        self._user_repository = user_repository

    async def get_user(self, user_id: int) -> User:
        return await self._user_repository.find_by_id(user_id=user_id)

    async def create_user(self, user: UserCreate) -> User:
        db_user = User(**user.model_dump())
        pass
