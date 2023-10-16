from contextvars import ContextVar, Token

"""
from asyncio import current_task => asyncio.gather()에서 Context-local을 보장할 수 없다.
하나의 Request가 들어올 때, uuid4 난수 값을 생성하고 미들웨어에서 ContextVar에 해당 값을 설정한다.
"""
async_session_context: ContextVar[str] = ContextVar("async_session_context")


def get_async_session_id() -> str:
    return async_session_context.get()


def set_async_session_context(session_id: str) -> Token:
    return async_session_context.set(session_id)


def reset_async_session_context(context: Token) -> None:
    async_session_context.reset(context)
