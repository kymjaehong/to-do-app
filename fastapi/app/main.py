import time
from fastapi import FastAPI, Request, Depends
from fastapi.middleware import Middleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging

from app.api.router import v1_router
from app.core.middleware.sqlalchemy import SQLAlchemyMiddleware
from app.core.dependency_container import Container
from app.api.api_response import ApiResponse
from app.adapter.orm import todo_orm_mapper

from app.core.security.token import MyValidateToken


# setup loggers
logging.config.fileConfig("app/core/config/logger.conf", disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)

# token dependency
my_validate_token = MyValidateToken()

app = FastAPI(
    title="To-Do App",
    middleware=[Middleware(cls=SQLAlchemyMiddleware)],
    dependencies=[Depends(my_validate_token)],
)
dependency_container = Container()
app.container = dependency_container

# imperative orm mappter (classic)
todo_orm_mapper()


@app.exception_handler(RequestValidationError)
async def exception_handler(request: Request, e: RequestValidationError):
    error = e.errors()[0]
    error_type = error["type"]
    error_loc = error["loc"]
    error_msg = error["msg"]

    return JSONResponse(
        ApiResponse.error(
            status_code=404, message=f"{error_type}: {error_loc}, {error_msg}"
        ).__dict__
    )


@app.exception_handler(Exception)
async def exception_handler(request: Request, e: Exception):
    return JSONResponse(ApiResponse.error(status_code=404, message=e.args[0]).__dict__)


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
