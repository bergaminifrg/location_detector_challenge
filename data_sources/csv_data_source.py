
import csv
from data_sources.ip_data_source import IPDataSource

class CSVDataSource(IPDataSource):
    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    def get_location_by_ip(self, ip):
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ip'] == ip:
                    return {
                        'latitude': row['latitude'],
                        'longitude': row['longitude'],
                        'country': row['country'],
                        'state': row['state'],
                        'city': row['city']
                    }