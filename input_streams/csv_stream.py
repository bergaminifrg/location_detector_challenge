import csv
from input_streams.input_stream import InputStream

class CSVStream(InputStream):
    def open(self):
        super().open()

    def read_input(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield {'id': row['id'], 'timestamp': int(row['timestamp']), 'ip': row['ip']}