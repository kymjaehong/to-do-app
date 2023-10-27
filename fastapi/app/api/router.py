from fastapi import APIRouter
from app.api.v1.endpoint.todo import todo_router
from app.api.v1.endpoint.user import user_router

v1_router = APIRouter()
v1_router.include_router(todo_router)
v1_router.include_router(user_router)
