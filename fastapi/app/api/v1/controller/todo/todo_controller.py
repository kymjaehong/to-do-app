from fastapi import Depends, APIRouter
from sqlalchemy.sql import func
from dependency_injector.wiring import Provide, inject

from app.core.dependency_container import Container

from app.domain.todo.todo_schema import ToDoCreate, ToDoSchema
from app.domain.todo.todo_service import ToDoService
from app.api.usecase.get_todo_by_user import GetToDoByUserUsecase
from app.api.usecase.register_todo import RegisterToDoUsecase
from app.api.usecase.get_todo_by_cond import GetToDoByCondUsecase

router = APIRouter()


@router.get("/{user_id}", response_model=list[ToDoSchema])
@inject
async def get_todo_list(
    user_id: int,
    get_todo_by_user_usecase: GetToDoByUserUsecase = Depends(
        Provide[Container.get_todo_by_user_usecase]
    ),
) -> list[ToDoSchema]:
    return await get_todo_by_user_usecase.execute(user_id=user_id)


@router.get("/{user_id}/search", response_model=list[ToDoSchema])
@inject
async def search_todo_list(
    user_id: int,
    keyword: str,
    get_todo_by_cond_usecase: GetToDoByCondUsecase = Depends(
        Provide[Container.get_todo_by_cond_usecase]
    ),
) -> list[ToDoSchema]:
    return await get_todo_by_cond_usecase.execute(user_id=user_id, keyword=keyword)


@router.post("/{user_id}", response_model=ToDoSchema)
@inject
async def register_todo(
    user_id: int,
    to_do_create: ToDoCreate,
    register_todo_usecase: RegisterToDoUsecase = Depends(
        Provide[Container.register_todo_user_usecase]
    ),
) -> ToDoSchema:
    created_now = func.now()
    return await register_todo_usecase.execute(
        user_id=user_id, to_do_create=to_do_create, created_now=created_now
    )


@router.patch("/complete/{to_do_id}", response_model=ToDoSchema)
@inject
async def update_todo(
    to_do_id: int,
    todo_service: ToDoService = Depends(Provide[Container.todo_service]),
) -> ToDoSchema:
    return await todo_service.update_todo(to_do_id=to_do_id)
