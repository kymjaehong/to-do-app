from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

from db.database import Base

if TYPE_CHECKING:
    from domain.todo.models import ToDo


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String(13), unique=True, index=True, nullable=False)
    name = Column(String(10), index=True)

    to_do_list = relationship(
        "ToDo", back_populates="user", cascade="all, delete, delete-orphan"
    )
