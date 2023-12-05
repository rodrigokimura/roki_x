import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from config.keys import KEYS
from config.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_app():
    assert isinstance(app, FastAPI)


def test_index(client: TestClient):
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers.get("content-type") == "text/html; charset=utf-8"


def test_keys(client: TestClient):
    response = client.get("/keys")

    assert response.status_code == 200
    assert len(response.json()) == len(KEYS)
