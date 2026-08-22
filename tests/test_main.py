from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "database": "connected",
    }


def test_create_item():
    response = client.post(
        "/items",
        json={
            "name": "Automated Test Item",
            "description": "Created by pytest",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Automated Test Item"
    assert data["description"] == "Created by pytest"
    assert "id" in data


def test_get_items():
    response = client.get("/items")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_item():
    create_response = client.post(
        "/items",
        json={
            "name": "Item Before Update",
            "description": "Original description",
        },
    )

    assert create_response.status_code == 200

    item_id = create_response.json()["id"]

    response = client.put(
        f"/items/{item_id}",
        json={
            "name": "Item After Update",
            "description": "Updated description",
        },
    )

    assert response.status_code == 200
    assert response.json()["id"] == item_id
    assert response.json()["name"] == "Item After Update"
    assert response.json()["description"] == "Updated description"

    client.delete(f"/items/{item_id}")


def test_delete_item():
    create_response = client.post(
        "/items",
        json={
            "name": "Item To Delete",
            "description": "Temporary item",
        },
    )

    assert create_response.status_code == 200

    item_id = create_response.json()["id"]

    response = client.delete(f"/items/{item_id}")

    assert response.status_code == 200
    assert response.json()["id"] == item_id


def test_update_nonexistent_item():
    response = client.put(
        "/items/999999",
        json={
            "name": "Does Not Exist",
            "description": "Should return 404",
        },
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item 999999 not found",
    }


def test_delete_nonexistent_item():
    response = client.delete("/items/999999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item 999999 not found",
    }