from abc import ABC, abstractmethod
from typing import Union
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
)
from sqlalchemy import select
from sqlalchemy.orm import lazyload, contains_alias, contains_eager, joinedload

from app.domain.todo import ToDo
from app.domain.user import User


class AbstractToDoRepostiroy(ABC):
    @abstractmethod
    async def find_by_id(self) -> ToDo:
        raise NotImplementedError

    @abstractmethod
    async def find_all_by_user(self) -> list[ToDo]:
        raise NotImplementedError

    @abstractmethod
    async def find_all_by_user_and_is_completed(self) -> list[ToDo]:
        raise NotImplementedError

    @abstractmethod
    async def save(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all_by_user_and_keyword(self) -> list[ToDo]:
        raise NotImplementedError


class ToDoRepository(AbstractToDoRepostiroy):
    def __init__(self, async_db: Union[AsyncSession, async_scoped_session]):
        self._db = async_db

    async def find_by_id(self, to_do_id: int) -> ToDo:
        todo = await self._db.scalar(select(ToDo).where(ToDo.id == to_do_id))
        if todo is None:
            raise Exception(f"not found by id {to_do_id}")
        return todo

    """
    N:1 관계에서 lazy loading을 하지 않으면, 무한 루프에 빠지게 된다.
    """

    async def find_all_by_user(self, user: User) -> list[ToDo]:
        stmt = select(ToDo).options(lazyload(ToDo.user)).where(ToDo.user_id == user.id)
        todo_list = await self._db.scalars(stmt)
        return todo_list.unique().all()

    async def find_all_by_user_and_is_completed(
        self, user: User, is_completed: bool | None
    ) -> list[ToDo]:
        stmt = select(ToDo).options(lazyload(ToDo.user)).where(ToDo.user == user)
        """
        [lazy load]
        N:1 관계에서 1의 조건을 확인하려면,
        직접 join을 해야 하는 것 같다.

        contains_eager는 에러가 발생하며,
        직접 join을 하지 않고 쓰면, 이상한 User를 가져온다...
        """
        multi_where_stmt = (
            select(ToDo)
            .outerjoin(User)
            .where(ToDo.user == user)
            .where(User.name.like("%" + "홍" + "%"))
            .options(contains_alias(ToDo.user))
        )
        """
        동적 쿼리 생성 방법을 아직은 모르겠다.
        사실 JPA도 이런 방법인거 같다.
        """
        if is_completed is not None:
            stmt = stmt.where(ToDo.is_complete == is_completed)

        todo_list = await self._db.scalars(stmt)
        """
        만약 service 계층에서 데이터 변환이 필요할 땐,
        scalars() 타입으로 return 하면 된다.

        unique().all() or all() 할 필요가 없다.
        """
        return todo_list.unique().all()

    async def save(self, to_do: ToDo):
        async with self._db as session:
            session.add(to_do)
            await session.commit()

    async def find_all_by_user_and_keyword(
        self, user: User, keyword: str
    ) -> list[ToDo]:
        stmt = (
            select(ToDo)
            .options(lazyload(ToDo.user))
            .where(ToDo.user == user)
            .where(ToDo.content.like("%" + keyword + "%"))
        )
        todo_list = await self._db.scalars(stmt)
        return todo_list.all()
