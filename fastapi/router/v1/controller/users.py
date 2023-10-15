from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from core.database.database import db_get, db_session
from router.v1.schemas.users import User
from application.service.users import UserService

router = APIRouter()

user_service = UserService()


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(db_get)) -> User:
    db_session.set(db)
    return user_service.get_user(user_id=user_id)


@router.get("/{phone_number}", response_model=User)
def get_user(phone_number: str, db: Session = Depends(db_get)) -> User:
    pass
