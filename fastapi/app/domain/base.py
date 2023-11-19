from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr


class BaseMixIn:
    @declared_attr
    def created_at(cls):
        return mapped_column(DateTime, nullable=False, server_default=func.now())

    @declared_attr
    def modified_at(cls):
        return mapped_column(
            DateTime,
            nullable=False,
            server_default=func.now(),
            server_onupdate=func.now(),
        )


class Base(DeclarativeBase, BaseMixIn):
    pass
