import time
import jwt

"""
Security
"""
SECRET_KEY = "World!"
ALGORITHM = "HS256"


class ValidateToken:
    not_access_url_path = False
    # 토큰 검증 요청 시간
    iat = time.time()

    def __call__(self, request: dict):
        NOT_ACCESS_URL_PATH = {
            "user": [],
            "todo": ["/"],
        }

        print(f"url check: {request.url.path}")
        request_url_path = request.url.path
        """
        /api/v1/user/...
        """
        url_path_list = request_url_path.split("/")

        """
        1. root url path가 아닌 경우
        2. 허용되지 않는 url path에 포함되는 경우
        """
        if (
            url_path_list[3] not in NOT_ACCESS_URL_PATH.keys()
            and url_path_list[4] in NOT_ACCESS_URL_PATH[url_path_list[3]]
        ):
            # 토큰 검증을 거치지 않는 URL
            self.not_allow_url_path = True

        """
        헤더에서 토큰 가져오기

        fastapi에서 제공하는 OAuth~Bearer를 사용하면, 이런 구현은 필요 없다.
        """
        headers = request.scope["headers"]

        for header in headers:
            if header[0].decode("utf-8") == "authorization":
                value: list[str] = header[1].decode("utf-8").split(" ")

                if value[0] == "Bearer":
                    print(f"now access token type >>> {value[1]}")

                    get_user_id = self.validate_token(access_token=value[1])
                    if get_user_id is None:
                        raise jwt.PyJWTError("확인되지 않은 회원 아이디입니다.")
                else:
                    raise jwt.PyJWTError("잘못된 암호 알고리즘입니다.")

    def validate_token(self, access_token: str) -> int | None:
        to_decode = jwt.decode(jwt=access_token, key=SECRET_KEY, algorithms=ALGORITHM)
        print(f"해독 >>>> {to_decode}")

        if to_decode["expiration_at"] > self.iat:
            print(f"토큰 만료 전 입니다 >>> {to_decode['user_id']}")
            return to_decode["user_id"]

        else:
            raise jwt.ExpiredSignatureError("토큰이 만료되었습니다.")
