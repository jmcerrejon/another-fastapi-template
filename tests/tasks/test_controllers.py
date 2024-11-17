from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException
from sqlalchemy.orm import Session

import src.tasks.models as models
from src.tasks import schemas
from src.tasks.controllers import (
    create_task,
    delete_task,
    get_task,
    get_task_list,
    update_task,
)


def test_get_task_list_success():
    session = MagicMock(spec=Session)
    task_list = [
        models.Task(id=1, task="Test Task 1"),
        models.Task(id=2, task="Test Task 2"),
    ]
    session.query().all.return_value = task_list

    result = get_task_list(session)

    assert result == task_list
    session.query().all.assert_called_once()


def test_get_task_list_exception():
    session = MagicMock(spec=Session)
    session.query().all.side_effect = Exception("Database error")

    with pytest.raises(HTTPException) as exc_info:
        get_task_list(session)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "You can't get the tasks list or It's empty."
    session.query().all.assert_called_once()


def test_get_task_success():
    session = MagicMock(spec=Session)
    task = models.Task(id=1, task="Test Task")
    session.get.return_value = task

    result = get_task(1, session)

    assert isinstance(result, schemas.OkResponse)
    assert result.id == 1
    assert result.task == "Test Task"
    session.get.assert_called_once_with(models.Task, 1)


def test_get_task_not_found():
    session = MagicMock(spec=Session)
    session.get.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        get_task(1, session)

    assert exc_info.value.status_code == 404
    session.get.assert_called_once_with(models.Task, 1)


def test_create_task_success():
    session = MagicMock(spec=Session)
    task_create = schemas.TaskCreate(task="New Task")

    session.add.return_value = None
    session.commit.return_value = None
    session.refresh.return_value = None
    session.refresh.side_effect = lambda x: setattr(x, "id", 1)

    result = create_task(task_create, session)

    assert isinstance(result, schemas.OkResponse)
    assert result.id == 1
    assert result.task == "New Task"
    session.add.assert_called_once()
    session.commit.assert_called_once()
    session.refresh.assert_called_once()


def test_create_task_exception():
    session = MagicMock(spec=Session)
    task_create = schemas.TaskCreate(task="New Task")

    session.add.side_effect = Exception("Database error")

    with pytest.raises(HTTPException) as exc_info:
        create_task(task_create, session)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Error creating task: Database error"
    session.add.assert_called_once()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_update_task_success():
    session = MagicMock(spec=Session)
    task_db = models.Task(id=1, task="Old Task")
    session.get.return_value = task_db

    result = update_task(1, "Updated Task", session)

    assert result.task == "Updated Task"
    session.get.assert_called_once_with(models.Task, 1)
    session.commit.assert_called_once()


def test_update_task_not_found():
    session = MagicMock(spec=Session)
    session.get.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        update_task(1, "Updated Task", session)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Task with id 1 not found"
    session.get.assert_called_once_with(models.Task, 1)
    session.commit.assert_not_called()


def test_delete_task_success():
    session = MagicMock(spec=Session)
    task_db = models.Task(id=1, task="Test Task")
    session.get.return_value = task_db

    result = delete_task(1, session)

    assert result is None
    session.get.assert_called_once_with(models.Task, 1)
    session.delete.assert_called_once_with(task_db)
    session.commit.assert_called_once()


def test_delete_task_not_found():
    session = MagicMock(spec=Session)
    session.get.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        delete_task(1, session)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Task with id 1 not found"
    session.get.assert_called_once_with(models.Task, 1)
    session.delete.assert_not_called()
    session.commit.assert_not_called()
