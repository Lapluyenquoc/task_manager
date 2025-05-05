# Task Management API

A REST API for managing personal tasks and projects, built with FastAPI, PostgreSQL, and JWT authentication.

- User authentication with JWT
- CRUD operations for tasks and projects
- Task filtering by status
- Project organization
- Secure password hashing
- Swagger UI documentation

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd task-management-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following content:
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/taskmanager
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Create the PostgreSQL database:
```bash
createdb taskmanager
```

## Running the Application

1. Start the server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- POST /register - Register a new user
- POST /login - Login and get JWT token
- GET /me - Get current user information

### Tasks
- POST /api/v1/tasks/ - Create a new task
- GET /api/v1/tasks/ - List all tasks
- GET /api/v1/tasks/{id} - Get task by ID
- PUT /api/v1/tasks/{id} - Update task
- DELETE /api/v1/tasks/{id} - Delete task

### Projects
- POST /api/v1/projects/ - Create a new project
- GET /api/v1/projects/ - List all projects
- GET /api/v1/projects/{id} - Get project by ID
- DELETE /api/v1/projects/{id} - Delete project

## Running Tests

```bash
pytest
```

## Code Quality

To check code quality with pylint:
```bash
pylint app > pylint.txt
```

## Project Structure

```
task-management-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── tasks.py
│   │   └── projects.py
│   └── auth/
│       ├── __init__.py
│       └── auth.py
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_tasks.py
├── requirements.txt
├── .env
└── README.md
``` 