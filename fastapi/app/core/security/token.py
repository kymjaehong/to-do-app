import time
import jwt
from fastapi import security, Request


"""
Security
"""
SECRET_KEY = "World!"
ALGORITHM = "HS256"
oauth2_scheme = security.OAuth2PasswordBearer(tokenUrl="token")


class ValidateToken:
    access_url_path = False
    # 토큰 검증 요청 시간
    iat = time.time()

    def __call__(self, request: Request):
        ACCESS_URL_PATH = {
            "user": ["login"],
            # "todo": [],
        }

        request_url_path = request.url.path

        """
        /api/v1/user/...
        """
        url_path_list = request_url_path.split("/")
        print(f"split / url: {url_path_list}")

        if (
            url_path_list[3] in ACCESS_URL_PATH.keys()
            and url_path_list[4] in ACCESS_URL_PATH[url_path_list[3]]
        ):
            # 토큰 검증을 거치지 않는 URL
            print(f"토큰 검증을 거치지 않는 URL Path: {request_url_path}")
            self.access_url_path = True

        """
        허용되는 url은 pass
        """
        if self.access_url_path:
            return

        """
        헤더에서 토큰 가져오기

        fastapi에서 제공하는 OAuth~Bearer를 사용하면, 이런 구현은 필요 없다.
        """
        headers = request.scope["headers"]
        authorization_check = False  # 토큰 확인

        for header in headers:
            if header[0].decode("utf-8") == "authorization":
                authorization_check = True
                value: list[str] = header[1].decode("utf-8").split(" ")

                if value[0] == "Bearer":
                    print(f"now access token type >>> {value[1]}")

                    get_user_id = self.validate_token(access_token=value[1])
                    if get_user_id is None:
                        raise jwt.PyJWTError("확인되지 않은 회원 아이디입니다.")
                else:
                    raise jwt.PyJWTError("잘못된 암호 알고리즘입니다.")
        if not authorization_check:
            raise jwt.PyJWTError("토큰이 필요합니다.")

    def validate_token(self, access_token: str) -> int | None:
        to_decode = jwt.decode(jwt=access_token, key=SECRET_KEY, algorithms=ALGORITHM)
        print(f"해독 >>>> {to_decode}")

        if to_decode["expiration_at"] > self.iat:
            print(f"토큰 만료 전 입니다 >>> {to_decode['user_id']}")
            return to_decode["user_id"]

        else:
            raise jwt.ExpiredSignatureError("토큰이 만료되었습니다.")
