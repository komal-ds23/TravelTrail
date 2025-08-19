
import os
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from traveltail.services import get_flight_provider, get_hotel_provider, build_recommendations

app = FastAPI(title="TravelTrail")

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
def index():
    with open(os.path.join(static_dir, "index.html"), "r", encoding="utf-8") as f:
        return f.read()

@app.get("/travel/flights")
def flights(origin: str = Query(...), destination: str = Query(...),
            start: str = Query(...), end: str = Query(...)):
    provider = get_flight_provider()
    data = [f.__dict__ for f in provider.search(origin, destination, start, end)]
    return JSONResponse(content=data)

@app.get("/travel/hotels")
def hotels(city: str = Query(...), checkin: str = Query(...), checkout: str = Query(...)):
    provider = get_hotel_provider()
    data = [h.__dict__ for h in provider.search(city, checkin, checkout)]
    return JSONResponse(content=data)

@app.get("/travel/recommendations")
def recommendations(origin: str = Query(...), destination: str = Query(...),
                    start: str = Query(...), end: str = Query(...),
                    city: str = Query(...), checkin: str = Query(...), checkout: str = Query(...)):
    recos = build_recommendations(origin, destination, start, end, city, checkin, checkout)
    data = [{
        "flight": r.flight.__dict__,
        "hotel": r.hotel.__dict__,
        "total_cost_usd": r.total_cost_usd,
        "total_time_minutes": r.total_time_minutes,
        "loyalty_score": r.loyalty_score,
        "score": r.score
    } for r in recos[:5]]
    return JSONResponse(content=data)
