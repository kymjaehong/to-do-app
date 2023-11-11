import time
from jose import jwt
from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from dependency_injector.wiring import Provide, inject

from app.core.dependency_container import Container
from app.service.user import UserService
from app.api.v1.request.user_request import UserCommand, LoginCommand
from app.api.api_response import ApiResponse

user_router = APIRouter(prefix="/user", tags=["user"])

"""
토큰
"""
ACCESS_TOKEN_EXPIRATION_MINUTES = 15 * 60
SECRET_KEY = "World!"
ALGORITHM = "HS256"


@user_router.post("/", response_model=ApiResponse)
@inject
async def register(
    command: UserCommand,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> ApiResponse:
    res = await user_service.create_user(command=command)
    return ApiResponse.ok(data=jsonable_encoder(res))


@user_router.get("/{user_id}", response_model=ApiResponse)
@inject
async def get_user(
    user_id: int, user_service: UserService = Depends(Provide[Container.user_service])
) -> ApiResponse:
    res = await user_service.get_user(user_id=user_id)
    return ApiResponse.ok(data=jsonable_encoder(res))


def generate_access_token(iat: float, user_id: int) -> str:
    payload = {
        "iss": "토큰 발급자의 해당 서비스 계정",
        "sub": "토큰 제목, 옵션",
        # "scope": "사용하고자 하는 API 권한",
        # "aud": "토큰 인증 서버 -> 해당 정보가 있으면 해당 서버로 인증 요청이 간다.",
        "iat": iat,
        "expiration_at": iat + ACCESS_TOKEN_EXPIRATION_MINUTES,
        "user_id": user_id,
    }
    additional_headers = {"kid": "인증 서버 private key id"}
    encoded_jwt = jwt.encode(
        payload, SECRET_KEY, algorithm=ALGORITHM, headers=additional_headers
    )
    return encoded_jwt


@user_router.post("/login", response_model=ApiResponse)
@inject
async def login(
    command: LoginCommand,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> ApiResponse:
    iat = time.time()
    res = await user_service.get_user(user_id=command.user_id)
    if res:
        """
        refresh token을 사용한다면, 추가 생성
        """
        access_token = generate_access_token(iat=iat, user_id=command.user_id)
        return ApiResponse.ok(data=jsonable_encoder(access_token))
    else:
        return ApiResponse.error(status_code=404, message="존재하지 않는 아이디입니다.")
