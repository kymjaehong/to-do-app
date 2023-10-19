from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy import func

from app.domain.user import User
from app.domain.todo import ToDo
from app.core.database.database import mapper_registry

user_table = Table(
    "users",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("phone_number", String(13), nullable=False, unique=True, index=True),
    Column("name", String(10), nullable=False),
)


todo_table = Table(
    "to_do",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("content", String(255), nullable=False),
    Column("is_complete", Boolean, nullable=False, default=False),
    Column("created", DateTime, nullable=False, default=func.now()),
    Column("user_id", Integer, ForeignKey("users.id")),
)


def todo_orm_mapper():
    mapper_registry.map_imperatively(
        User,
        user_table,
        properties={"todo_list": relationship(ToDo, backref="users")},
    )
    mapper_registry.map_imperatively(
        ToDo,
        todo_table,
        properties={"user": relationship(User, backref="to_do")},
    )
