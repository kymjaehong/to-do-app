from uuid import uuid4
from starlette.types import ASGIApp, Receive, Scope, Send

from app.core.database.async_session import (
    set_async_session_context,
    reset_async_session_context,
)
from app.core.database.database import async_session


class SQLAlchemyMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        session_id = str(uuid4())
        context = set_async_session_context(session_id=session_id)
        print(f"middleware call >> async mysql id=({id(self)})")

        try:
            await self.app(scope, receive, send)
        except Exception as e:
            await async_session.rollback()
            raise e
        finally:
            await async_session.remove()
            reset_async_session_context(context=context)
