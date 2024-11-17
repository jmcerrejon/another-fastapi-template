from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException
from sqlalchemy.orm import Session

import src.tasks.models as models
from src.tasks import schemas
from src.tasks.controllers import create_task, get_task, get_task_list, update_task


def test_get_task_list_success():
    # Arrange
    session = MagicMock(spec=Session)
    task_list = [
        models.Task(id=1, task="Test Task 1"),
        models.Task(id=2, task="Test Task 2"),
    ]
    session.query().all.return_value = task_list

    # Act
    result = get_task_list(session)

    # Assert
    assert result == task_list
    session.query().all.assert_called_once()


def test_get_task_list_exception():
    # Arrange
    session = MagicMock(spec=Session)
    session.query().all.side_effect = Exception("Database error")

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        get_task_list(session)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "You can't get the tasks list or It's empty."
    session.query().all.assert_called_once()


def test_get_task_success():
    # Arrange
    session = MagicMock(spec=Session)
    task = models.Task(id=1, task="Test Task")
    session.query().get.return_value = task

    # Act
    result = get_task(1, session)

    # Assert
    assert result == schemas.OkResponse(**task.__dict__)
    session.query().get.assert_called_once_with(1)


def test_get_task_not_found():
    # Arrange
    session = MagicMock(spec=Session)
    session.query().get.return_value = None

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        get_task(1, session)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Task with id 1 not found"
    session.query().get.assert_called_once_with(1)
