from typing import Generator

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from src.utils.logger import logger


class SingletonMeta(type):
    """
    Metaclass to implement the Singleton pattern.
    """

    _instances: dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    __DATABASE_URL = "sqlite:///./DB.db"

    def __init__(self):
        self.url = self.__DATABASE_URL
        self.engine = create_engine(self.url)
        self.Base = declarative_base()
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        logger.info("Database initialized.")

    def create_tables(self) -> None:
        if inspect(self.engine).has_table("tasks"):
            return None

        self.Base.metadata.create_all(bind=self.engine)
        logger.info("Tables created.")

    def get_db(self) -> Generator[Session, None, None]:
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
