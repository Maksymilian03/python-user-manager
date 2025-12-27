from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_user_success():
    response = client.post(
        "/users",
        json={"email": "test@wp.pl"}
    )
    assert response.status_code == 201
    assert response.json() == {"message": "User created"}


def test_create_duplicate_user_unsuccess():
    email = "dup_test@wp.pl"

    client.post("/users",json={"email": email})

    response = client.post(
        "/users",
        json={"email": email}
    )

    assert response.status_code == 400
    assert "detail" in response.json()

def test_delete_user_success():
    email = "delete_test@wp.pl"
    client.post("/users", json={"email": email})

    response = client.delete(f"/users/{email}")

    assert response.status_code == 200
    assert "message" in response.json()

def test_delete_user_not_found():

    response = client.delete(f"/users/notfound@wp.pl")

    assert response.status_code == 404

def test_get_users_success():

    response = client.get("/users")

    assert response.status_code == 200