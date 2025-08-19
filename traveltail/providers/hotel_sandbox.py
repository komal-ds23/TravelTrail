
import json, os
from typing import List
from ..models import Hotel
from .base import HotelProvider

class SandboxHotelProvider(HotelProvider):
    def __init__(self, data_path: str):
        self.data_path = data_path

    def search(self, city: str, checkin: str, checkout: str) -> List[Hotel]:
        fp = os.path.join(self.data_path, "hotels.json")
        with open(fp, "r") as f:
            data = json.load(f)
        hotels = []
        for d in data:
            if d["city"].lower() == city.lower():
                hotels.append(Hotel(**d))
        return hotels
