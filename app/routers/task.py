# app/routers/task.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import task as schemas
from app.controllers import task as crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task, user_id=user_id)