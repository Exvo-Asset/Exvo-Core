from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_list_assets():
r = client.get('/v1/assets/')
assert r.status_code == 200
assert isinstance(r.json(), list)
