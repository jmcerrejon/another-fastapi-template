from pydantic import BaseModel, ConfigDict


class OkResponse(BaseModel):
    id: int
    task: str


class TaskCreate(BaseModel):
    task: str


class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    task: str
