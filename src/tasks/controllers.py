from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import src.tasks.models as models
from src.tasks import schemas


def get_task_list(session: Session):
    try:
        task_list = session.query(models.Task).all()
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str("You can't get the tasks list or It's empty."),
        )
    return task_list


def get_task(id: int, session: Session):
    task = session.query(models.Task).get(id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found"
        )
    return schemas.OkResponse(**task.__dict__)


def create_task(task: schemas.TaskCreate, session: Session):
    task_db = models.Task(task=task.task)
    session.add(task_db)
    session.commit()
    session.refresh(task_db)
    return schemas.OkResponse(**task_db.__dict__)


def update_task(id: int, task: str, session: Session):
    task_db = session.query(models.Task).get(id)
    if task_db:
        task_db.task = task
        session.commit()
    if not task_db:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")
    return task_db


def delete_task(id: int, session: Session):
    task_db = session.query(models.Task).get(id)
    if not task_db:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")
    session.delete(task_db)
    session.commit()
    return None
