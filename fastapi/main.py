from fastapi import FastAPI

from api.router.api import api_router
from db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do App")

app.include_router(api_router, prefix="/api/v1")
