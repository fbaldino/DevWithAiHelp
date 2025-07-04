import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from hello_app import app


def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b'Hello, World!'
