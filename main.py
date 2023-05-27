import sys
import os
from pathlib import Path
from strategies.csv_location_strategy import CSVLocationStrategy
from strategies.database_location_strategy import DatabaseLocationStrategy
from services.location_service import LocationService
from data_sources.csv_data_source import CSVDataSource
from data_sources.sqlite_data_source import SQLiteDataSource
from input_streams.csv_stream import CSVStream as CSVInputStream
from input_streams.json_stream import JSONStream as JSONInputStream
from output_streams.csv_stream import CSVStream as CSVOutputStream
from output_streams.json_stream import JSONStream as JSONOutputStream
from utils.utils import is_within_time_window
from app import App

translation_type = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

input_stream_mapping = {
    '.csv': CSVInputStream,
    '.jsonl': JSONInputStream,
}

input_file_extension = Path(input_file).suffix
print(Path(input_file).suffix)
input_stream_type = input_stream_mapping[input_file_extension]

if input_stream_type is None:
    print(f"Invalid input file extension: {input_file_extension}")
    sys.exit(1)

input_stream = input_stream_type(input_file)

output_stream_mapping = {
    '.csv': CSVOutputStream,
    '.jsonl': JSONOutputStream,
}

output_file_extension = Path(output_file).suffix
output_stream_type = output_stream_mapping.get(output_file_extension)

if output_stream_type is None:
    print(f"Invalid output file extension: {output_file_extension}")
    sys.exit(1)

output_stream = output_stream_type(output_file)

translation_type_mapping = {
    'csv': CSVLocationStrategy(
        CSVDataSource(
            os.path.abspath("IPs.csv"))),
    'database': DatabaseLocationStrategy(
        SQLiteDataSource(
            os.path.abspath("IPs.sqlite")))
}

location_service = LocationService(
    translation_type_mapping.get(translation_type))

app = App(location_service, input_stream, output_stream)

time_window_minutes = 30
time_window_ms = time_window_minutes * 60 * 1000

app.process_messages(time_window_ms)