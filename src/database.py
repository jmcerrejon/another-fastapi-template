from functools import lru_cache as singleton
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


@singleton
class Database:
    __DATABASE_URL = "sqlite:///./DB.db"

    def __init__(self):
        self.url = self.__DATABASE_URL
        self.engine = create_engine(self.url)
        self.Base = declarative_base()
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def create_tables(self) -> None:
        self.Base.metadata.create_all(bind=self.engine)

    def get_db(self) -> Generator[Session, None, None]:
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
