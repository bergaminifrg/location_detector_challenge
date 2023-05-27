from utils.utils import is_within_time_window, format_latitude_longitude
class App:
    def __init__(self, location_service, input_stream, output_stream):
        self.location_service = location_service
        self.input_stream = input_stream
        self.output_stream = output_stream
    
    def process_messages(self, time_window_ms):
        processed_ips = {}
        
        for message in self.input_stream.read_input():
            id = message['id']
            ip = message['ip']
            timestamp = message['timestamp']
            
            if (ip in processed_ips
                    and is_within_time_window(timestamp, processed_ips[ip]['timestamp'], time_window_ms)):
                location = processed_ips[ip]
            else:
                location = self.location_service.get_location(ip)

            if not location:
                continue

            output_message = {
                'id': id,
                'timestamp': timestamp,
                'ip': ip,
                'latitude': format_latitude_longitude(location['latitude']),
                'longitude': format_latitude_longitude(location['longitude']),
                'country': location['country'],
                'state': location['state'],
                'city': location['city']
            }
            
            processed_ips[ip] = output_message
            self.output_stream.write_output(output_message)