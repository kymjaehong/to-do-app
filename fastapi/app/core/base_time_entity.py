from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import declared_attr


class BaseTimeEntity:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=func.now(), nullable=False)

    @declared_attr
    def modified_at(cls):
        return Column(
            DateTime,
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )
