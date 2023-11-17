from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    create_async_engine,
)
from typing import Union

from app.core.config import config
from app.core.database.async_session import get_async_session_id
from app.core.database.sync_session import get_sync_session_id

MYSQL_SYNC_URL = f"{config.SYNC_ENGINE}://{config.USERNAME}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.NAME}"

sync_engine = create_engine(MYSQL_SYNC_URL, echo=True)
sync_session_factory = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)
sync_session: Union[Session, scoped_session] = scoped_session(
    session_factory=sync_session_factory, scopefunc=get_sync_session_id
)

MYSQL_ASYNC_URL = f"{config.ASYNC_ENGINE}://{config.USERNAME}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.NAME}"

async_engine = create_async_engine(MYSQL_ASYNC_URL, echo=True)
async_session_factory = sessionmaker(
    class_=AsyncSession, autocommit=False, autoflush=False, bind=async_engine
)
async_session: Union[AsyncSession, async_scoped_session] = async_scoped_session(
    session_factory=async_session_factory, scopefunc=get_async_session_id
)
