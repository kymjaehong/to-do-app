from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String

from app.domain.todo import ToDo

from app.domain.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)

    todos: Mapped[list[ToDo]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, phone_number={self.phone_number!r}, created_at={self.created_at!r}, modified_at={self.modified_at!r})"
