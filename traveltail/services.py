
import os
from typing import List
from .models import Flight, Hotel, Recommendation
from .ranking import rank_recommendations
from .providers.flight_sandbox import SandboxFlightProvider
from .providers.hotel_sandbox import SandboxHotelProvider

DATA_PATH = os.environ.get("TRAVELTRAIL_DATA", os.path.join(os.path.dirname(__file__), "..", "mock_data"))

def get_flight_provider():
    return SandboxFlightProvider(DATA_PATH)

def get_hotel_provider():
    return SandboxHotelProvider(DATA_PATH)

def build_recommendations(origin: str, destination: str, start: str, end: str, city: str, checkin: str, checkout: str, weights=None) -> List[Recommendation]:
    flights = get_flight_provider().search(origin, destination, start, end)
    hotels  = get_hotel_provider().search(city, checkin, checkout)
    recos: List[Recommendation] = []
    for f in flights:
        for h in hotels:
            total_cost = f.price_usd + h.price_usd
            total_time = f.duration_minutes + h.nights * 60
            loyalty = (len(f.airline) % 5) / 5.0 + h.rating / 5.0
            recos.append(Recommendation(
                flight=f, hotel=h,
                total_cost_usd=total_cost,
                total_time_minutes=total_time,
                loyalty_score=loyalty,
                score=0.0
            ))
    return rank_recommendations(recos, weights=weights)
