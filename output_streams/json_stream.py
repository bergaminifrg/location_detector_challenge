import json
from output_streams.output_stream import OutputStream

class JSONStream(OutputStream):
    def open(self):
        super().open()

    def write_output(self, message):
        with open(self.file_path, 'a') as file:
            json.dump(message, file, default=str)
            file.write('\n')