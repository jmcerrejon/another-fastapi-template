import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.tasks.models import Base, Task

DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="module")
def engine():
    return create_engine(DATABASE_URL)


@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="module")
def session(engine, tables):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def test_task_model(session):
    new_task = Task(task="Test Task")
    session.add(new_task)
    session.commit()

    retrieved_task = session.query(Task).filter_by(task="Test Task").first()
    assert retrieved_task is not None
    assert retrieved_task.task == "Test Task"
