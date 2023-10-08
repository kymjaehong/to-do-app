from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config.config import MYSQL_DATABASE_URL

Base = declarative_base()

engine = create_engine(MYSQL_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def db_get():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
