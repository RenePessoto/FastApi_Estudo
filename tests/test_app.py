from fastapi.testclient import TestClient
from fast_zero.app import app
from http import HTTPStatus


def test_read_root_deve_retornar_OK_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "Hello World!"}
