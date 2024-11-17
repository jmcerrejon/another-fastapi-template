import pytest
from pydantic import ValidationError

from src.tasks.schemas import OkResponse, Task, TaskCreate


def test_ok_response():
    response = OkResponse(id=1, task="Test Task")
    assert response.id == 1
    assert response.task == "Test Task"


def test_ok_response_invalid():
    with pytest.raises(ValidationError):
        OkResponse(id="one", task="Test Task")


def test_task_create():
    task_create = TaskCreate(task="New Task")
    assert task_create.task == "New Task"


def test_task_create_invalid():
    with pytest.raises(ValidationError):
        TaskCreate(task=123)


def test_task():
    task = Task(id=1, task="Existing Task")
    assert task.id == 1
    assert task.task == "Existing Task"


def test_task_invalid():
    with pytest.raises(ValidationError):
        Task(id="one", task="Existing Task")
