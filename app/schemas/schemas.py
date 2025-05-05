from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.models import TaskStatus

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    title: str
    deadline: datetime
    status: TaskStatus
    project_id: int

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    deadline: Optional[datetime] = None
    status: Optional[TaskStatus] = None
    project_id: Optional[int] = None

class Task(TaskBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True 