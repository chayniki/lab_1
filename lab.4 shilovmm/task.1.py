import json

FILENAME = "input.json"

def task() -> float:
    """
    Функция для вычисления суммы произведений (score * weight).
    """

    with open(FILENAME, 'r') as input_f:

        data = json.load(input_f)

    multiple = [round(items['score'] * items['weight'], 3) for items in data]

    return sum(multiple)

print(task())
