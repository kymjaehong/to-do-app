from fastapi import APIRouter
from app.api.v1.controller.todo import todo_controller
from app.api.v1.controller.users import user_controller

v1_router = APIRouter()
v1_router.include_router(user_controller.router, prefix="/user", tags=["users"])
v1_router.include_router(todo_controller.router, prefix="/to-do", tags=["to-do"])
