import json


def load_data():
    with open('data.json', 'rb') as f:
        data = json.load(f)
        return data


def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)