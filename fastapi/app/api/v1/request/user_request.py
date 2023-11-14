from dataclasses import dataclass


@dataclass
class UserCommand:
    phone_number: str
    name: str

    def __post_init__(self):
        if len(self.phone_number.split("-")) != 3:
            raise ValueError("올바른 핸드폰 번호가 아닙니다.")
        if len(self.phone_number) > 13:
            raise ValueError("올바른 핸드폰 번호가 아닙니다.")


@dataclass
class LoginCommand:
    user_id: int
