import csv
from output_streams.output_stream import OutputStream

class CSVStream(OutputStream):
    headers_written = False
    def open(self):
        super().open()

    def write_output(self, message):
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=message.keys())
            if not self.headers_written:
                writer.writeheader()
                self.headers_written = True
            writer.writerow(message)