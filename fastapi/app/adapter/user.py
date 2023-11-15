from abc import ABC, abstractmethod
from typing import Union
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
)
from sqlalchemy import select
from sqlalchemy.orm import joinedload, contains_eager, with_loader_criteria

from app.domain.user import User
from app.domain.todo import ToDo


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
        eager_stmt = (
            select(User).options(joinedload(User.todo_list)).where(User.id == user_id)
        )
        """
        [eager load]
        orm mapping에서 연관된 테이블의 where 절을 사용해야 할 때,
        직접 join을 해야 한다.
        직접 join을 하지 않으면, 이상한 객체를 가져온다. (eager load도 이와 같다.)

        eager loading의 경우, joinedload 대신 contains_eager를 사용한다.
        명시적 조인을 했을 때, joinedload를 사용하면 조인이 두 번 발생한다.
        """
        multi_where_stmt = (
            select(User)
            .outerjoin(ToDo)
            .options(
                with_loader_criteria(ToDo, ToDo.is_complete == True),
                contains_eager(User.todo_list),
            )
            .where(User.id == user_id)
        )
        user = await self._db.execute(eager_stmt)
        return user.scalar()

    async def save(self, user: User) -> None:
        async with self._db as session:
            session.add(user)
            await session.commit()
