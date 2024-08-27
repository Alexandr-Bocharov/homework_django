import json
import random


def write_data(data_new: dict):
    try:
        with open('data/data.json', 'r') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = {}

    id = random.randint(1, 99999999)

    data[id] = data_new

    with open('data/data.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print('Запись прошла успешно')