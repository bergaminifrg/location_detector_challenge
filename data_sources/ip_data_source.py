from abc import ABC, abstractmethod

class IPDataSource(ABC):
    @abstractmethod
    def get_location_by_ip(self, ip):
        pass