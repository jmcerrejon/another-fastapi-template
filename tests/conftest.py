import pytest

from src.database import Database


@pytest.fixture(scope="session", autouse=True)
def dispose_database():
    """Release the pooled database connections when the test session ends."""
    yield
    Database().dispose()
