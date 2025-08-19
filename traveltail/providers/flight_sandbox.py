
import json, os
from typing import List
from ..models import Flight
from .base import FlightProvider

class SandboxFlightProvider(FlightProvider):
    def __init__(self, data_path: str):
        self.data_path = data_path

    def search(self, origin: str, destination: str, start: str, end: str) -> List[Flight]:
        fp = os.path.join(self.data_path, "flights.json")
        with open(fp, "r") as f:
            data = json.load(f)
        flights = []
        for d in data:
            if d["origin"] == origin and d["destination"] == destination:
                flights.append(Flight(**d))
        return flights
