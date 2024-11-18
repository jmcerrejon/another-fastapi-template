import inspect

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import src.tasks.models as models
from src.tasks import schemas
from src.utils.logger import logger


def get_task_list(session: Session):
    try:
        task_list = session.query(models.Task).all()
    except Exception:
        exception = {
            "source": f"{__name__} > {inspect.currentframe().f_code.co_name}",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": "You can't get the tasks list or It's empty.",
        }
        logger.error(exception)
        raise HTTPException(
            status_code=int(exception.get("status_code", 500)),
            detail=exception.get("detail"),
        )

    return task_list


def get_task(id: int, session: Session):
    task = session.get(models.Task, id)
    if task is None:
        exception = {
            "source": f"{__name__} > {inspect.currentframe().f_code.co_name}",
            "status_code": status.HTTP_404_NOT_FOUND,
            "detail": f"Task with id {id} not found.",
        }
        logger.error(exception)
        raise HTTPException(
            status_code=int(exception.get("status_code", 404)),
            detail=exception.get("detail"),
        )

    return schemas.OkResponse(**task.__dict__)


def create_task(task: schemas.TaskCreate, session: Session):
    try:
        task_db = models.Task(task=task.task)
        session.add(task_db)
        session.commit()
        session.refresh(task_db)
    except Exception as e:
        exception = {
            "source": f"{__name__} > {inspect.currentframe().f_code.co_name}",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": f"Error creating task: {str(e)}.",
        }
        logger.error(exception)
        raise HTTPException(
            status_code=int(exception.get("status_code", 500)),
            detail=exception.get("detail"),
        )

    return schemas.OkResponse(**task_db.__dict__)


def update_task(id: int, task: str, session: Session):
    task_db = session.get(models.Task, id)
    if task_db:
        task_db.task = task
        session.commit()
    if not task_db:
        exception = {
            "source": f"{__name__} > {inspect.currentframe().f_code.co_name}",
            "status_code": status.HTTP_404_NOT_FOUND,
            "detail": f"Task with id {id} not found.",
        }
        logger.error(exception)
        raise HTTPException(
            status_code=int(exception.get("status_code", 404)),
            detail=exception.get("detail"),
        )

    return task_db


def delete_task(id: int, session: Session):
    task_db = session.get(models.Task, id)
    if not task_db:
        exception = {
            "source": f"{__name__} > {inspect.currentframe().f_code.co_name}",
            "status_code": status.HTTP_404_NOT_FOUND,
            "detail": f"Task with id {id} not found.",
        }
        logger.error(exception)
        raise HTTPException(
            status_code=exception.get("status_code", 404),
            detail=exception.get("detail"),
        )
    session.delete(task_db)
    session.commit()

    return None
