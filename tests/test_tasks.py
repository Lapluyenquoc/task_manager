import pytest
from fastapi.testclient import TestClient
from datetime import datetime, timedelta
from app.main import app
from app.models.models import TaskStatus

client = TestClient(app)

def get_auth_token(client):
    # Register and login to get token
    client.post(
        "/register",
        json={"username": "taskuser", "password": "taskpass"}
    )
    response = client.post(
        "/login",
        data={"username": "taskuser", "password": "taskpass"}
    )
    return response.json()["access_token"]

def test_create_task(client):
    token = get_auth_token(client)
    task_data = {
        "title": "Test Task",
        "deadline": (datetime.now() + timedelta(days=1)).isoformat(),
        "status": TaskStatus.TODO,
        "project_id": 1
    }
    
    response = client.post(
        "/api/v1/tasks/",
        json=task_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["status"] == task_data["status"]

def test_get_tasks(client):
    token = get_auth_token(client)
    response = client.get(
        "/api/v1/tasks/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_task_by_id(client):
    token = get_auth_token(client)
    # First create a task
    task_data = {
        "title": "Test Task 2",
        "deadline": (datetime.now() + timedelta(days=1)).isoformat(),
        "status": TaskStatus.TODO,
        "project_id": 1
    }
    create_response = client.post(
        "/api/v1/tasks/",
        json=task_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    task_id = create_response.json()["id"]
    
    # Then get it by id
    response = client.get(
        f"/api/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == task_data["title"]

def test_update_task(client):
    token = get_auth_token(client)
    # First create a task
    task_data = {
        "title": "Test Task 3",
        "deadline": (datetime.now() + timedelta(days=1)).isoformat(),
        "status": TaskStatus.TODO,
        "project_id": 1
    }
    create_response = client.post(
        "/api/v1/tasks/",
        json=task_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    task_id = create_response.json()["id"]
    
    # Update the task
    update_data = {
        "title": "Updated Task",
        "status": TaskStatus.IN_PROGRESS
    }
    response = client.put(
        f"/api/v1/tasks/{task_id}",
        json=update_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_data["title"]
    assert data["status"] == update_data["status"]

def test_delete_task(client):
    token = get_auth_token(client)
    # First create a task
    task_data = {
        "title": "Test Task 4",
        "deadline": (datetime.now() + timedelta(days=1)).isoformat(),
        "status": TaskStatus.TODO,
        "project_id": 1
    }
    create_response = client.post(
        "/api/v1/tasks/",
        json=task_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    task_id = create_response.json()["id"]
    
    # Delete the task
    response = client.delete(
        f"/api/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 204
    
    # Verify task is deleted
    get_response = client.get(
        f"/api/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_response.status_code == 404 