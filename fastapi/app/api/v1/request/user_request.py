from dataclasses import dataclass


@dataclass
class UserCommand:
    phone_number: str
    name: str
