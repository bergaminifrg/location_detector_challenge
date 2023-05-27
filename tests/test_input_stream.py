import unittest
from input_streams.json_stream import JSONStream
from input_streams.csv_stream import CSVStream

class InputStreamTests(unittest.TestCase):
    def test_json_stream_read_input(self):
        file_path = './example_files/input_example.jsonl'
        stream = JSONStream(file_path)
        messages = list(stream.read_input())
        
        self.assertEqual(len(messages), 225)
        
        self.assertEqual(messages[0]['id'], '1a301e29-6d6f-5e47-b130-e8fb5c0b1ee2')
        self.assertEqual(messages[0]['timestamp'], 1684196387094)
        self.assertEqual(messages[0]['ip'], '59.90.255.63')
        
        self.assertEqual(messages[-1]['id'], 'ee526cba-4846-5a1f-bd30-5397a63ce383')
        self.assertEqual(messages[-1]['timestamp'], 1684205871074)
        self.assertEqual(messages[-1]['ip'], None)

    def test_csv_stream_read_input(self):
        file_path = './example_files/input_example.csv'
        stream = CSVStream(file_path)
        messages = list(stream.read_input())
        
        self.assertEqual(len(messages), 225)
        
        self.assertEqual(messages[0]['id'], '1a301e29-6d6f-5e47-b130-e8fb5c0b1ee2')
        self.assertEqual(messages[0]['timestamp'], 1684196387094)
        self.assertEqual(messages[0]['ip'], '59.90.255.63')
        
        self.assertEqual(messages[-1]['id'], 'ee526cba-4846-5a1f-bd30-5397a63ce383')
        self.assertEqual(messages[-1]['timestamp'], 1684205871074)
        self.assertEqual(messages[-1]['ip'], '')

if __name__ == '__main__':
    unittest.main()