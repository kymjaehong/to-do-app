from contextvars import ContextVar
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from typing import Union

from core.config import config

MYSQL_DATABASE_URL = f"{config.DB_ENGINE}://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

engine = create_engine(MYSQL_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def db_get():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
    finally:
        db.close()


db_session: ContextVar[Session] = ContextVar("db_session")


def get_session_id() -> str:
    return db_session.get()


session: Union[Session, scoped_session] = scoped_session(
    session_factory=SessionLocal, scopefunc=get_session_id
)
