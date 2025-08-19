
# TravelTrail

Create a service that calls free-tier (or sandbox) flight/hotel APIs, ranks options by cost, time, and loyalty, and displays results in a web UI.

## Features
- **Flight API**: `GET /travel/flights?from=&to=&start=&end=`
- **Hotel API**: `GET /travel/hotels?city=&checkin=&checkout=`
- **Recommendation API**: Combines & ranks results (weighted formula), returns top 5.
- **Web UI**: Simple HTML/JS page with a search form and sortable table.
- **Testing**: Unit tests for ranking and API endpoints using mocks.
- **Mock data**: `mock_data/flights.json`, `mock_data/hotels.json`

## Quickstart (local)
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
# open http://127.0.0.1:8000/
```

## Switching to real free-tier APIs
This repo uses a sandbox provider by default. To integrate real free-tier providers (e.g., Amadeus sandbox, Skyscanner sandbox):
- Create new provider classes under `traveltail/providers/` that implement `FlightProvider` / `HotelProvider`.
- Read API keys from environment variables.
- Swap `get_flight_provider()` / `get_hotel_provider()` in `services.py` based on env flags.

## Ranking formula
Min-max normalize cost (↓ better), total time (↓ better), and loyalty (↑ better). Weighted score defaults to:
```
score = 0.5*(1 - cost_norm) + 0.3*(1 - time_norm) + 0.2*(loyalty_norm)
```
Tune with query params or code.

## Tests
```bash
pytest -q
```

## Deliverables
- Code for API & UI
- Mock datasets (sample responses)
- README and prompt_log
- You can capture UI screenshots from the running app.
