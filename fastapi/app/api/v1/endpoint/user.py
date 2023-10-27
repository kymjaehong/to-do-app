from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from dependency_injector.wiring import Provide, inject

from app.core.dependency_container import Container
from app.service.user import UserService
from app.api.v1.request.user_request import UserCommand
from app.api.api_response import ApiResponse

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.post("/", response_model=ApiResponse)
@inject
async def register(
    command: UserCommand,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> ApiResponse:
    res = await user_service.create_user(command=command)
    return ApiResponse.ok(data=jsonable_encoder(res))


@user_router.get("/{user_id}", response_model=None)
@inject
async def get_user(
    user_id: int, user_service: UserService = Depends(Provide[Container.user_service])
) -> ApiResponse:
    res = await user_service.get_user(user_id=user_id)
    return ApiResponse.ok(data=jsonable_encoder(res))
