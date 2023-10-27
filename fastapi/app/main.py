import time
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware import Middleware

from app.api.router import v1_router
from app.core.middleware.sqlalchemy import SQLAlchemyMiddleware
from app.core.dependency_container import Container
from app.api.api_response import ApiResponse
from app.adapter.orm import todo_orm_mapper

from app.core.security.token import ValidateToken

# token dependency
valid_token = ValidateToken()

app = FastAPI(
    title="To-Do App",
    middleware=[Middleware(cls=SQLAlchemyMiddleware)],
    dependencies=[Depends(valid_token)],
)
dependency_container = Container()
app.container = dependency_container

# imperative orm mappter (classic)
todo_orm_mapper()


# 토큰 핸들러 수정 필요함!!!!!!!!!!!!!!
# @app.exception_handler(Exception)
# async def bankx_exception_handler(request: Request, e: Exception):
#     return ApiResponse.error(status_code=405, message=e.args[0])


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    print(
        f"{request.method} {request.url}\nrunning time: {time.time() - start_time} sec"
    )
    return response


app.include_router(
    v1_router,
    prefix="/api/v1",
)
