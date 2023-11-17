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
        stmt = select(ToDo).where(ToDo.id == to_do_id)
        todo = await self._db.execute(stmt)
        todo = todo.scalar()
        if todo is None:
            raise Exception(f"not found by id {to_do_id}")
        return todo

    async def find_all_by_user(self, user: User) -> list[ToDo]:
        stmt = select(ToDo).where(ToDo.user_id == user.id)
        todo_list = await self._db.execute(stmt)
        return todo_list.scalars().unique().all()

    async def find_all_by_user_and_is_completed(
        self, user: User, is_completed: bool | None
    ) -> list[ToDo]:
        stmt = select(ToDo).where(ToDo.user == user)
        """
        [lazy load]
        N:1 관계에서 1의 조건을 확인하려면,
        직접 join을 해야 한다.

        contains_eager는 joinedload와 마찬가지로 무한 루프 에러가 발생한다.
        """
        multi_where_stmt = (
            select(ToDo)
            .outerjoin(User)
            .where(ToDo.user == user, User.name.like("%" + "홍" + "%"))
        )
        """
        동적 쿼리 생성 방법을 아직은 모르겠다.
        사실 JPA도 이런 방법인거 같다.
        """
        if is_completed is not None:
            stmt = stmt.where(ToDo.is_complete == is_completed)

        todo_list = await self._db.execute(stmt)

        return todo_list.scalars().unique().all()

    async def save(self, to_do: ToDo):
        async with self._db as session:
            session.add(to_do)
            await session.commit()

    """
    selectinload가 N+1 문제를 해결할 수 있다고 한다. (one to many 관계)
    하지만, many to one 관계에서 selectinload를 사용하면, 무한 루프 에러가 발생한다.
    
    joinedload 또한 무한 루프가 발생한다.
    selectinload는 in절을 활용한다.
    """

    async def find_all_by_user_and_keyword(
        self, user: User, keyword: str
    ) -> list[ToDo]:
        stmt = (
            select(ToDo)
            # .options(lazyload(ToDo.user)) # 작성하지 않아도 지연 로딩이 된다.
            .where(ToDo.user == user, ToDo.content.like("%" + keyword + "%"))
        )
        todo_list = await self._db.execute(stmt)
        return todo_list.scalars().unique().all()
