from typing import Union
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
)
from sqlalchemy import select

from app.domain.todo.todo import ToDo
from app.domain.users.users import User


class ToDoRepository:
    def __init__(self, async_db: Union[AsyncSession, async_scoped_session]):
        self._db = async_db

    async def find_by_id(self, to_do_id: int) -> ToDo:
        row_todo = await self._db.execute(
            select(ToDo).join(ToDo.user).where(ToDo.id == to_do_id)
        )
        todo = row_todo.scalar()
        if todo is None:
            raise Exception(f"not found by id {to_do_id}")
        return todo

    async def find_all_by_user(self, user: User) -> list[ToDo]:
        row_todo_list = self._db.execute(select(ToDo).where(ToDo.user == user))
        todo_list = row_todo_list.scalars().all()
        return todo_list

    async def save(self, to_do: ToDo) -> ToDo:
        self._db.add(to_do)
        self._db.commit()
        self._db.refresh(to_do)
        return to_do

    async def find_all_by_user_and_keyword(
        self, user: User, keyword: str
    ) -> list[ToDo]:
        row_todo_list = await self._db.execute(
            select(ToDo)
            .where(ToDo.user == user)
            .where(ToDo.content.like("%" + keyword + "%"))
        )
        todo_list = row_todo_list.scalars().all()
        return todo_list
