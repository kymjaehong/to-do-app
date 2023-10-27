from abc import ABC, abstractmethod
from typing import Union
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
)
from sqlalchemy import select
from sqlalchemy.orm import lazyload

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
        print(f"parameter user: {user}")
        todo_list = await self._db.scalars(
            select(ToDo).options(lazyload(ToDo.user)).where(ToDo.user_id == user.id)
        )
        return todo_list.unique().all()

    async def save(self, to_do: ToDo):
        async with self._db as session:
            session.add(to_do)
            await session.commit()

    async def find_all_by_user_and_keyword(
        self, user: User, keyword: str
    ) -> list[ToDo]:
        todo_list = await self._db.scalars(
            select(ToDo)
            .options(lazyload(ToDo.user))
            .where(ToDo.user == user)
            .where(ToDo.content.like("%" + keyword + "%"))
        )
        return todo_list.all()
