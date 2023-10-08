from fastapi import APIRouter
from api.router.v1 import user, todo

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["users"])
api_router.include_router(todo.router, prefix="/to-do", tags=["to-do"])
