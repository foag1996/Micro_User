# import pytest
# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)


# def test_index_route():
#     response = client.get('/items/1')
#     assert response.status_code == 200


import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/infoUser/foag')
    assert response.status_code == 200

def test_204():
    response = client.get('/infoUser/foag')
    assert response.status_code == 204