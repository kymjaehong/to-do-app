from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db.database import db_get

from domain.users.schemas import User
import api.service.user

router = APIRouter()


@router.get("/{phone_number}", response_model=User)
def get_user(phone_number: str, db: Session = Depends(db_get)) -> User:
    user = api.service.user.get_user(db=db, phone_number=phone_number)
    return user
