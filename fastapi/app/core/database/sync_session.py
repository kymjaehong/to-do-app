from contextvars import ContextVar, Token

sync_session_context: ContextVar[str] = ContextVar("sync_session_context")


def get_sync_session_id() -> str:
    return sync_session_context.get()


def set_sync_session_context(session_id: str) -> Token:
    return sync_session_context.set(session_id)


def reset_sync_session_context(context: Token) -> None:
    sync_session_context.reset(context)
