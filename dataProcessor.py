import json
import pandas as pd

def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

            if(len(data) == 0):
                raise ValueError(f"Json Vazio: {file_path}")

            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    

def avgAgeCountry(path):

    json = pd.read_json(path)

    return json['age'].mean()

def filter_by_age(path, age: int):

    json = pd.read_json(path)

    return json.query(f'age >= {age}')

    

    