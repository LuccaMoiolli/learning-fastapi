from fastapi.testclient import TestClient
from fast.henlo import app


def test_if_henlo_is_ok():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == 200