from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from core.database.database import Base


class ToDo(Base):
    __tablename__ = "to_do"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(255), nullable=False)
    is_complete = Column(Boolean, nullable=False, default=False)
    created = Column(DateTime(timezone=True), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="to_do_list")

    @classmethod
    def _validate(cls) -> bool:
        return True

    @classmethod
    def create(cls, content: str, created: DateTime, user_id: int) -> "ToDo":
        if not cls._validate():
            raise Exception("validate Exception")
        return cls(content=content, created=created, user_id=user_id)

    def update_is_complete(self):
        self.is_complete = not self.is_complete
