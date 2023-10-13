import time
from fastapi import FastAPI, Request

from routes.v1.router import v1_router
from database import Base, engine


app = FastAPI(title="To-Do App")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    print(
        f"{request.method} {request.url}\nrunning time: {time.time() - start_time} sec"
    )
    return response


def init_db():
    print("init database")
    Base.metadata.create_all(bind=engine)


# init_db() # I only do it at first time
app.include_router(v1_router, prefix="/api/v1")
