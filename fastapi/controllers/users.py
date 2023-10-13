from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database import db_get

from schemas.users import User
from service import users

router = APIRouter()


@router.get("/{phone_number}", response_model=User)
def get_user(phone_number: str, db: Session = Depends(db_get)) -> User:
    user = users.get_user(db=db, phone_number=phone_number)
    return user
