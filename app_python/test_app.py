from app import app as test_app
from datetime import datetime
import json


def test_app_is_running():
    client = test_app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200


def test_app_returns_local_in_iso():
    client = test_app.test_client()
    url = '/'

    response = client.get(url)
    response_json = json.loads(response.data.decode())
    assert datetime.fromisoformat(response_json["local time"])


def test_app_returns_utc_in_iso():
    client = test_app.test_client()
    url = '/'
    response = client.get(url)
    response_json = json.loads(response.data.decode())
    assert datetime.fromisoformat(response_json["utc time"])
