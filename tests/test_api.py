
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_flights_endpoint():
    r = client.get("/travel/flights", params={"origin":"SFO","destination":"LAX","start":"2025-09-01","end":"2025-09-05"})
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert all(d["origin"]=="SFO" and d["destination"]=="LAX" for d in data)

def test_hotels_endpoint():
    r = client.get("/travel/hotels", params={"city":"Los Angeles","checkin":"2025-09-01","checkout":"2025-09-05"})
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert all(d["city"]=="Los Angeles" for d in data)

def test_recommendations_endpoint():
    r = client.get("/travel/recommendations", params={
        "origin":"SFO","destination":"LAX","start":"2025-09-01","end":"2025-09-05",
        "city":"Los Angeles","checkin":"2025-09-01","checkout":"2025-09-05"
    })
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) <= 5
