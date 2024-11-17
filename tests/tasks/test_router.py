from typing import Any

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from main import app
from src.tasks.schemas import Task

client = TestClient(app)


@pytest.fixture
def sample_task():
    return Task(id=1, task="Sample Task")


@pytest.fixture
def create_task(sample_task: Task) -> None:
    response = client.post("/tasks/", json=sample_task.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    return response.json()


def test_read_task_list(create_task: Any) -> None:
    response = client.get("/tasks")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_create_task(create_task: Any) -> None:
    response = client.get(f"/tasks/{create_task.get('id')}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == create_task


def test_read_task(create_task: Any) -> None:
    task_id = create_task.get("id")
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("id") == task_id
    assert response.json().get("task") == create_task.get("task")


def test_read_task_not_found() -> None:
    response = client.get("/tasks/9999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_task(create_task: Any) -> None:
    task_id = create_task.get("id")
    updated_task = "Updated Task"
    response = client.put(f"/tasks/{task_id}?task={updated_task}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("task") == updated_task


def test_update_task_not_found() -> None:
    updated_task = "Updated Task"
    response = client.put(f"/tasks/9999?task={updated_task}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_task(create_task: Any) -> None:
    task_id = create_task.get("id")
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verify the task is actually deleted
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_task_not_found() -> None:
    response = client.delete("/tasks/9999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
