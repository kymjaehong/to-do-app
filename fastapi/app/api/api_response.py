from typing import TypeVar
from dataclasses import dataclass, field

"""
Generic T 구현
"""
T = TypeVar("T")


@dataclass
class ApiResponse:
    status_code: int = 200
    message: str = "Ok"
    data: list | dict = field(default_factory=list)

    @classmethod
    def ok(cls, data: list | dict) -> "ApiResponse":
        return cls(data=data)

    @classmethod
    def error(cls, status_code: int, message: str) -> "ApiResponse":
        return cls(status_code=status_code, message=message)
