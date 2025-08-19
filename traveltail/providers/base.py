
from abc import ABC, abstractmethod
from typing import List
from ..models import Flight, Hotel

class FlightProvider(ABC):
    @abstractmethod
    def search(self, origin: str, destination: str, start: str, end: str) -> List[Flight]:
        ...

class HotelProvider(ABC):
    @abstractmethod
    def search(self, city: str, checkin: str, checkout: str) -> List[Hotel]:
        ...
