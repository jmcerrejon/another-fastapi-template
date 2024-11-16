from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import src.tasks.models as models
from src.database import get_db
from src.tasks import schemas

router = APIRouter()


@router.get(
    "/tasks",
    response_model=List[schemas.Task],
    summary="Get all tasks",
    description="Get all tasks from the database",
)
def read_task_list(session: Session = Depends(get_db)):
    try:
        task_list = session.query(models.Task).all()
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str("You can't get the tasks list or It's empty."),
        )

    return task_list


@router.get(
    "/tasks/{id}",
    response_model=schemas.Task,
    responses={
        status.HTTP_200_OK: {
            "model": schemas.OkResponse,
            "description": "Ok Response",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Task not found",
        },
    },
    summary="Get a task",
    description="Get a task by id",
)
def read_task(id: int, session: Session = Depends(get_db)):
    task = session.query(models.Task).get(id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found"
        )

    return schemas.OkResponse(**task.__dict__)


@router.post(
    "/tasks",
    response_model=schemas.Task,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
    description="Create a new task and return it",
)
def create_task(task: schemas.TaskCreate, session: Session = Depends(get_db)):
    task_db = models.Task(task=task.task)

    session.add(task_db)
    session.commit()
    session.refresh(task_db)

    return schemas.OkResponse(**task_db.__dict__)


@router.put(
    "/tasks/{id}",
    response_model=schemas.Task,
    responses={
        status.HTTP_200_OK: {
            "description": "Ok Response",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Task with that id not found",
        },
    },
    summary="Update a task",
    description="Update a task by id",
)
def update_task(id: int, task: str, session: Session = Depends(get_db)):
    task_db = session.query(models.Task).get(id)

    if task_db:
        task_db.task = task
        session.commit()

    if not task_db:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    return task_db


@router.delete(
    "/tasks/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {
            "description": "Task deleted",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Task with that id not found",
        },
    },
    summary="Delete a task",
    description="Delete a task by id",
)
def delete_task(id: int, session: Session = Depends(get_db)):
    task_db = session.query(models.Task).get(id)

    if not task_db:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    session.delete(task_db)
    session.commit()

    return None
