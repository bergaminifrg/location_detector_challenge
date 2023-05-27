import os
import unittest
from app import App
from input_streams.json_stream import JSONStream as JSONInputStream
from input_streams.csv_stream import CSVStream as CSVInputStream
from output_streams.json_stream import JSONStream as JSONOutputStream
from output_streams.csv_stream import CSVStream as CSVOutputStream
from data_sources.sqlite_data_source import SQLiteDataSource
from data_sources.csv_data_source import CSVDataSource
from services.location_service import LocationService
from strategies.database_location_strategy import DatabaseLocationStrategy
from strategies.csv_location_strategy import CSVLocationStrategy
import json
import pandas as pd

class IntegrationTest(unittest.TestCase):
    thirty_minutes_in_ms = 30 * 60 * 1000
    def test_integration_from_json(self):
        input_file = "./example_files/input_example.jsonl"
        input_stream = JSONInputStream(input_file)

        output_file = "tests/output_files/output.jsonl"
        output_stream = JSONOutputStream(output_file)

        database_file = os.path.abspath("IPs.sqlite")
        sqlite_data_source = SQLiteDataSource(database_file)

        location_strategy = DatabaseLocationStrategy(sqlite_data_source)

        location_service = LocationService(location_strategy)

        app = App(location_service, input_stream, output_stream)

        app.process_messages(self.thirty_minutes_in_ms)

        with open(output_file, "r") as f:
            generated_data = [json.loads(line) for line in f]

        with open('example_files/output_example.jsonl', "r") as f:
            example_data = [json.loads(line) for line in f]

        self.assertEqual(generated_data, example_data, "Generated data is not the same as the example data")

        os.remove(output_file)

    def test_integration_from_csv(self):
        input_file = "./example_files/input_example.csv"
        input_stream = CSVInputStream(input_file)

        output_file = "tests/output_files/output.csv"
        output_stream = CSVOutputStream(output_file)

        database_file = os.path.abspath("IPs.csv")
        csv_data_source = CSVDataSource(database_file)

        location_strategy = CSVLocationStrategy(csv_data_source)

        location_service = LocationService(location_strategy)

        app = App(location_service, input_stream, output_stream)

        app.process_messages(self.thirty_minutes_in_ms)

        self.assertTrue(compare_csv_files(output_file, 'example_files/output_example.csv'))
        
        os.remove(output_file)


def compare_csv_files(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    if set(df1.columns) != set(df2.columns):
        return False

    df1 = df1.reindex(sorted(df1.columns), axis=1)
    df2 = df2.reindex(sorted(df2.columns), axis=1)

    comparison = df1.values == df2.values

    if not comparison.all():
        return False

    return True

if __name__ == "__main__":
    unittest.main()
