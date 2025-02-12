# schemas/task.py
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True