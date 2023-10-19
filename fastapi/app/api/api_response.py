from pydantic import BaseModel, Field
from typing import TypeVar

T = TypeVar("T")


class ApiResponse(BaseModel):
    status_code: int = Field(default=200)
    message: str = Field(default="Ok")
    data: T = Field(default=[])

    @classmethod
    def ok(cls, data: T) -> "ApiResponse":
        return cls(status_code=200, message="Ok", data=data)

    @classmethod
    def error(cls, status_code: int, message: str) -> "ApiResponse":
        return cls(status_code=status_code, message=message, data=None)
