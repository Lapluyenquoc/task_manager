from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, tasks, projects
from app.database import engine
from app.models import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="A REST API for managing personal tasks and projects",
    version="1.0.0"
)
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include routers
app.include_router(auth.router, tags=["Authentication"])
app.include_router(tasks.router, prefix="/api/v1", tags=["Tasks"])
app.include_router(projects.router, prefix="/api/v1", tags=["Projects"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Management API"} 