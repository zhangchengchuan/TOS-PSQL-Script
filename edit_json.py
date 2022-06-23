import json


def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def change_json_file(file_path, configuration):
    with open(file_path, 'w') as f:
        json.dump(configuration, f, indent=4)
