import pytest
from fastapi.testclient import TestClient

def get_auth_token(client):
    # Register and login to get token
    client.post(
        "/register",
        json={"username": "projectuser", "password": "projectpass"}
    )
    response = client.post(
        "/login",
        data={"username": "projectuser", "password": "projectpass"}
    )
    return response.json()["access_token"]

def test_create_project(client):
    token = get_auth_token(client)
    project_data = {
        "name": "Test Project"
    }
    
    response = client.post(
        "/api/v1/projects/",
        json=project_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == project_data["name"]

def test_get_projects(client):
    token = get_auth_token(client)
    response = client.get(
        "/api/v1/projects/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_project_by_id(client):
    token = get_auth_token(client)
    # First create a project
    project_data = {
        "name": "Test Project 2"
    }
    create_response = client.post(
        "/api/v1/projects/",
        json=project_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    project_id = create_response.json()["id"]
    
    # Then get it by id
    response = client.get(
        f"/api/v1/projects/{project_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == project_data["name"]

def test_delete_project(client):
    token = get_auth_token(client)
    # First create a project
    project_data = {
        "name": "Test Project 3"
    }
    create_response = client.post(
        "/api/v1/projects/",
        json=project_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    project_id = create_response.json()["id"]
    
    # Delete the project
    response = client.delete(
        f"/api/v1/projects/{project_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 204
    
    # Verify project is deleted
    get_response = client.get(
        f"/api/v1/projects/{project_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_response.status_code == 404 