from sqlalchemy import Column, Integer, String

from src.database import Database

database = Database()
Base = database.Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task = Column(String(256))
