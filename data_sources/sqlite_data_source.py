import sqlite3
from data_sources.ip_data_source import IPDataSource

class SQLiteDataSource(IPDataSource):
    def __init__(self, db_file):
        self.db_file = db_file
    
    def get_location_by_ip(self, ip):
        conn = sqlite3.connect(self.db_file)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        #TODO get a better Select from database
        cursor.execute("SELECT latitude, longitude, country, state, city FROM IPs WHERE ip = ?", (ip,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return dict(result)
        return None