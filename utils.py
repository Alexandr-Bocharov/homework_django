import json
import random
import secrets
import string


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


def generation_password(symbols_num=10) -> str:
    letters = string.ascii_letters
    digits = string.digits
    alphabet = letters + digits

    new_password = ''

    for _ in range(symbols_num):
        new_password += secrets.choice(alphabet)

    return new_password

