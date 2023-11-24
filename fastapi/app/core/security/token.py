import time, logging
from jose import jwt
from fastapi import security, Request, Depends

logger = logging.getLogger(__name__)

"""
Security
"""
SECRET_KEY = "World!"
ALGORITHM = "HS256"
oauth2_scheme = security.OAuth2PasswordBearer(tokenUrl="token", auto_error=False)


async def get_token_data(request: Request, iat: float):
    # oauth 코드 활용
    authorization = request.headers["Authorization"]
    if authorization:
        scheme, _, param = authorization.partition(" ")
        logger.info(f"header: {scheme}, token: {param}")

        if param and scheme.lower() == "bearer":
            to_decode = jwt.decode(param, SECRET_KEY, algorithms=ALGORITHM)
            logger.info(f"만료일 확인 {to_decode['expiration_at']} > {iat}")
            if to_decode["expiration_at"] > iat:
                return to_decode["data"]


class ABCValidateToken:
    access_url_path = False
    # 토큰 검증 요청 시간
    iat = time.time()

    def validate_token(self, access_token: str | None):
        if not access_token and not self.access_url_path:
            raise Exception("토큰이 필요한 URL 입니다.")

        if access_token:
            to_decode = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            logger.info(f"해독 >>>> {to_decode}")

            if to_decode["expiration_at"] > self.iat:
                logger.info(f"토큰 만료 전 입니다 >>> {to_decode['user_id']}")
            else:
                """
                refresh token을 사용하면, 추가 로직 생성
                """
                raise jwt.ExpiredSignatureError("토큰이 만료되었습니다.")


class MyValidateToken(ABCValidateToken):
    def __init__(self):
        super().__init__()

    def __call__(
        self, request: Request, access_token: str | None = Depends(oauth2_scheme)
    ):
        ACCESS_URL_PATH = {
            "user": ["login", "register"],
            # "todo": [],
        }

        request_url_path = request.url.path

        """
        /api/v1/user/...
        """
        url_path_list = request_url_path.split("/")
        print(f"split / url: {url_path_list}")

        if (
            url_path_list[3] in ACCESS_URL_PATH
            and url_path_list[4] in ACCESS_URL_PATH[url_path_list[3]]
        ):
            # 토큰 검증을 거치지 않는 URL
            print(f"토큰 검증을 거치지 않는 URL Path: {request_url_path}")
            self.access_url_path = True

        # ABC 클래스
        self.validate_token(access_token=access_token)
