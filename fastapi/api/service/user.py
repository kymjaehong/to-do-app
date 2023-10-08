from sqlalchemy.orm import Session

from domain.users.models import User
from domain.users.schemas import UserCreate


def get_user(db: Session, phone_number: str) -> User:
    return db.query(User).filter(User.phone_number == phone_number).first()


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
