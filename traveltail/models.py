
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class Flight:
    id: str
    origin: str
    destination: str
    depart_at: str  # ISO date
    arrive_at: str  # ISO date
    duration_minutes: int
    price_usd: float
    airline: str

@dataclass
class Hotel:
    id: str
    city: str
    name: str
    checkin: str  # ISO date
    checkout: str  # ISO date
    nights: int
    price_usd: float
    rating: float  # 0-5

@dataclass
class Recommendation:
    flight: Flight
    hotel: Hotel
    total_cost_usd: float
    total_time_minutes: int
    loyalty_score: float
    score: float  # overall ranking score
