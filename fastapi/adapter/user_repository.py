from core.database.database import session
from domain.users import User


class UserRepository:
    def __init__(self):
        self._db = session

    def find_by_id(self, user_id: int) -> User:
        user = self._db.query(User).filter(User.id == user_id).one_or_none()
        if user is None:
            raise Exception(f"not found user by id: {user_id}")
        return user
