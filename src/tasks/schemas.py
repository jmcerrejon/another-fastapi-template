from pydantic import BaseModel


class OkResponse(BaseModel):
    id: int
    task: str


class TaskCreate(BaseModel):
    task: str


class Task(BaseModel):
    id: int
    task: str

    class Config:
        from_attributes = True
