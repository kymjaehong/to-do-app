from fastapi import APIRouter
from router.v1.controller import users, todo

v1_router = APIRouter()
v1_router.include_router(users.router, prefix="/user", tags=["users"])
v1_router.include_router(todo.router, prefix="/to-do", tags=["to-do"])
