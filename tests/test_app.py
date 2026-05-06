import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    res = client.get('/')
    assert res.status_code == 200
    data = res.get_json()
    assert data['status'] == 'ok'

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200