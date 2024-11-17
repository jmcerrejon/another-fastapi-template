from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.database import Database
from src.tasks import controllers, schemas

router = APIRouter()
get_db = Database().get_db


@router.get(
    "/tasks",
    response_model=List[schemas.Task],
    summary="Get all tasks",
    description="Get all tasks from the database",
)
def read_task_list(session: Session = Depends(get_db)):
    return controllers.get_task_list(session)


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
    return controllers.get_task(id, session)


@router.post(
    "/tasks",
    response_model=schemas.Task,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
    description="Create a new task and return it",
)
def create_task(task: schemas.TaskCreate, session: Session = Depends(get_db)):
    return controllers.create_task(task, session)


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
    return controllers.update_task(id, task, session)


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
    return controllers.delete_task(id, session)
