from dependency_injector import containers, providers

from app.core.database.database import async_session
from app.adapter.todo import ToDoRepository
from app.adapter.user import UserRepository
from app.service.todo import ToDoService
from app.service.user import UserService
from app.api.usecase.get_todo_by_user import GetToDoByUserUsecase
from app.api.usecase.register_todo import RegisterToDoUsecase
from app.api.usecase.get_todo_by_cond import GetToDoByCondUsecase


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoint.todo",
            "app.api.v1.endpoint.user",
        ]
    )

    # async db
    async_db = providers.Singleton(async_session)

    # repository
    user_repository = providers.Factory(UserRepository, async_db=async_db)
    todo_repository = providers.Factory(ToDoRepository, async_db=async_db)

    # service
    user_service = providers.Factory(UserService, user_repository=user_repository)
    todo_service = providers.Factory(ToDoService, todo_repository=todo_repository)

    # usecase
    get_todo_by_user_usecase = providers.Factory(
        GetToDoByUserUsecase, user_service=user_service, todo_service=todo_service
    )
    register_todo_user_usecase = providers.Factory(
        RegisterToDoUsecase, user_service=user_service, todo_service=todo_service
    )
    get_todo_by_cond_usecase = providers.Factory(
        GetToDoByCondUsecase, user_service=user_service, todo_service=todo_service
    )
