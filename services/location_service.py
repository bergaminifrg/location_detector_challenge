class LocationService:
    def __init__(self, location_strategy):
        self.location_strategy = location_strategy

    def get_location(self, ip_address):
        return self.location_strategy.get_location(ip_address)