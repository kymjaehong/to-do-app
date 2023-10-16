import time
from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
import asyncio

from app.api.router import v1_router
from app.core.database.database import Base, async_engine
from app.core.middleware.sqlalchemy import SQLAlchemyMiddleware
from app.core.dependency_container import Container


app = FastAPI(
    title="To-Do App",
    middleware=[Middleware(cls=SQLAlchemyMiddleware)],
)
dependency_container = Container()
app.container = dependency_container


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    print(
        f"{request.method} {request.url}\nrunning time: {time.time() - start_time} sec"
    )
    return response


"""
def init_sync_db():
    print("init database")
    Base.metadata.drop_all(bind=sync_engine)
    Base.metadata.create_all(bind=sync_engine)


init_sync_db
"""

"""
async def init_async_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(init_async_db())
"""

app.include_router(v1_router, prefix="/api/v1")
