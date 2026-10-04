from fastapi.testclient import TestClient
from entersrc.main import app

client = TestClient(app)


def test_answers_and_refuses():
    hit = client.post("/ask", json={"question": 'Which ticket is CrashLoopBackOff after a memory bump?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == "ticket"
    miss = client.post("/ask", json={"question": 'weather tomorrow'}).json()
    assert miss["answered"] is False


def test_empty_is_refused():
    assert client.post("/ask", json={"question": " "}).status_code == 422
