from app.adapter.user_repository import AbstractUserRepository
from app.domain.user import User
from app.api.v1.request.user_request import UserCommand


class UserService:
    def __init__(self, user_repository: AbstractUserRepository):
        self._user_repository = user_repository

    async def get_user(self, user_id: int) -> User:
        return await self._user_repository.find_by_id(user_id=user_id)

    async def create_user(self, command: UserCommand) -> None:
        user = User.create(command=command)
        return await self._user_repository.save(user=user)
