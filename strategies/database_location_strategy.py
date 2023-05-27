from strategies.location_strategy import LocationStrategy

class DatabaseLocationStrategy(LocationStrategy):
    def __init__(self, data_source):
        self.data_source = data_source

    def get_location(self, ip):
        return self.data_source.get_location_by_ip(ip)