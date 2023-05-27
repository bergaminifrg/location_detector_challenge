# Croct Location Detector Challenge

## Requirements
To run the application, you will need:
- Python

## Setup Instructions
1. **Python Libraries**: Install the required Python libraries by running the following command in your terminal or command prompt:
```
  pip install -r requirements.txt
```

2. **Running the Application**:
```
  python main.py {data_source} {input_file_path} {output_file_path}
```
The valid data source types are: csv | database

The valid input and output file types are '.csv' and '.jsonl'

Example:
```
python main.py database example_files/input_example.csv output.csv
```


3. **Tests**: Use the following command to run the tests:
```
  python -m unittest discover tests
```