from abc import ABC, abstractmethod
from typing import Union
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
)
from sqlalchemy import select

from app.domain.users.users import User


class AbstractUserRepository(ABC):
    @abstractmethod
    async def find_by_id(self) -> User:
        raise NotImplementedError


class UserRepository:
    def __init__(self, async_db: Union[AsyncSession, async_scoped_session]):
        self._db = async_db

    async def find_by_id(self, user_id: int) -> User:
        row_user = await self._db.execute(select(User).where(User.id == user_id))
        user = row_user.scalar()
        if user is None:
            raise Exception(f"not found user by id: {user_id}")
        return user
