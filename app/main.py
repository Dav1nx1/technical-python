# app/main.py
from fastapi import FastAPI
from app.routers import user, task
from app.database import engine, Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown

app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(task.router, prefix="/tasks", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management System"}