import unittest
import os
from output_streams.csv_stream import CSVStream
from output_streams.json_stream import JSONStream

class OutputStreamTests(unittest.TestCase):
    def test_csv_stream_write_output(self):
        file_path = 'tests/output_files/output.csv'
        output_stream = CSVStream(file_path)

        message = {
            "id": "1a301e29-6d6f-5e47-b130-e8fb5c0b1ee2",
            "timestamp": 1684196387094,
            "ip": "59.90.255.63",
            "latitude": "12.96677",
            "longitude": "77.58003",
            "country": "India",
            "state": "Karnataka",
            "city": "Bengaluru"
        }

        output_stream.open()
        output_stream.write_output(message)

        os.remove(file_path)

    def test_json_stream_write_output(self):
        file_path = 'tests/output_files/output.jsonl'
        output_stream = JSONStream(file_path)

        messages = {
            "id": "1a301e29-6d6f-5e47-b130-e8fb5c0b1ee2",
            "timestamp": 1684196387094,
            "ip": "59.90.255.63",
            "latitude": "12.96677",
            "longitude": "77.58003",
            "country": "India",
            "state": "Karnataka",
            "city": "Bengaluru"
        }
        
        output_stream.open()
        output_stream.write_output(messages)

        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()