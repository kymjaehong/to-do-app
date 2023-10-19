from fastapi import APIRouter
from app.api.v1.controller.todo_controller import todo_router
from app.api.v1.controller.user_controller import user_router

v1_router = APIRouter()
v1_router.include_router(todo_router)
v1_router.include_router(user_router)
