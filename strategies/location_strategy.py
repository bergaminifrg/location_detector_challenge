from abc import ABC, abstractmethod

class LocationStrategy(ABC):
    @abstractmethod
    def get_location(self, ip_address):
        pass