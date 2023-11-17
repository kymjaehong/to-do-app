from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer, Boolean, ForeignKey

from app.domain.base import Base


class ToDo(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    is_complete: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="todos", lazy=True)

    def __repr__(self) -> str:
        return f"ToDo(id={self.id!r}, content={self.content!r}, is_complete={self.is_complete!r}, created_at={self.created_at!r}, modified_at={self.modified_at!r})"

    def update_is_complete(self):
        self.is_complete = not self.is_complete
