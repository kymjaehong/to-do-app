from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import TYPE_CHECKING

from db.database import Base

if TYPE_CHECKING:
    from domain.users.models import User


class ToDo(Base):
    __tablename__ = "to_do"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255))
    is_complete = Column(Boolean, default=False)
    created = Column(DateTime(timezone=True), default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="to_do_list")
