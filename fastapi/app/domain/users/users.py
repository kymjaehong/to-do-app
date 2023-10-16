from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database.database import Base
from app.core.base_time_entity import BaseTimeEntity


# BaseTimeEntity 활용
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String(13), nullable=False, unique=True, index=True)
    name = Column(String(10), nullable=False)

    to_do_list = relationship(
        "ToDo", back_populates="user", cascade="all, delete, delete-orphan"
    )

    @classmethod
    def _validate(cls) -> bool:
        return True

    @classmethod
    def create(cls, phone_number: str, name: str) -> "User":
        if not cls._validate():
            raise Exception("validate Exception")
        return cls(phone_number=phone_number, name=name)
