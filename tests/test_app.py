import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from hello_app import app


def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'


def test_test_endpoint():
    response = app.test_client().get('/test')

    assert response.status_code == 200
    assert response.mimetype == 'text/plain'
    assert 'docker compose exec app pytest -q' in response.get_data(as_text=True)
