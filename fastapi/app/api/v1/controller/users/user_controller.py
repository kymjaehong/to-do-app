from fastapi import Depends, APIRouter
from dependency_injector.wiring import Provide, inject

from app.core.dependency_container import Container


from app.domain.users.user_schema import UserSchema
from app.domain.users.user_service import UserService

router = APIRouter()


@router.get("/{user_id}", response_model=UserSchema)
@inject
async def get_user(
    user_id: int, user_service: UserService = Depends(Provide[Container.user_service])
) -> UserSchema:
    return await user_service.get_user(user_id=user_id)


@router.get("/{phone_number}", response_model=UserSchema)
async def get_user(phone_number: str) -> UserSchema:
    pass
