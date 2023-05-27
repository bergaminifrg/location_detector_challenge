import json
from input_streams.input_stream import InputStream

class JSONStream(InputStream):
    def open(self):
        super().open()

    def read_input(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                data = json.loads(line)
                yield data
