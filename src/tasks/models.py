from sqlalchemy import Column, Integer, String

from src.database import Database

Base = Database().Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task = Column(String(256))
