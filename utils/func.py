import json


def load_operations():
    """
    Чтение файла JSON с операциями
    :return: список операций в формате dict
    """
    with open('../operations.json', encoding="utf-8") as file:
        operations = json.load(file)
        return operations


def sorting_of_executed():
    """
    Сортирует все операции на выявление выполненных и не выполненных
    :return: список выполненных операций
    """
    executed_operations = []
    operations = load_operations()
    for elements in operations:
        if elements.get("state") == "EXECUTED":
            executed_operations.append(elements)
    for value in executed_operations:
        if value == None:
            executed_operations.remove(value)
    return executed_operations





