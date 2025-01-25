from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.websocket_connect("/chat")
    assert response.application_state == "CONNECTED"
    
    response.send_text("Hello, test message")
    data = response.receive_text()
    assert len(data) > 0
    
    response.close()

def test_analytics_endpoint():
    response = client.get("/analytics/learning-progress")
    assert response.status_code == 200
    
    data = response.json()
    assert "avg_recall_accuracy" in data
    assert "avg_concept_retention" in data