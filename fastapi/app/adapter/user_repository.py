from abc import ABC, abstractmethod
from typing import Union
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
)
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.domain.user import User


class AbstractUserRepository(ABC):
    @abstractmethod
    async def find_by_id(self) -> User:
        raise NotImplementedError

    @abstractmethod
    async def save(self) -> None:
        raise NotImplementedError


class UserRepository:
    def __init__(self, async_db: Union[AsyncSession, async_scoped_session]):
        self._db = async_db

    """
    1:N관계에서 eager loading을 통해 매핑된 정보를 모두 가져올 수 있다.
    1에 대한 결과이기 때문에 scalar()를 사용하면 된다.
    """

    async def find_by_id(self, user_id: int) -> User:
        user = await self._db.scalar(
            select(User).options(joinedload(User.todo_list)).where(User.id == user_id)
        )
        return user

    async def save(self, user: User) -> None:
        async with self._db as session:
            session.add(user)
            await session.commit()
