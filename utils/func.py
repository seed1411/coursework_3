import json
import pathlib


def load_operations():
    """
    Чтение файла JSON с операциями
    :return: список операций в формате dict
    """
    path = pathlib.Path(__file__).parent.parent.joinpath("data").joinpath("operations.json")
    with open(path, encoding="utf-8") as file:
        operations = json.load(file)
        return operations


def sorting_of_executed():
    """
    Сортирует все операции на выявление выполненных и не выполненных
    :return: список из 5 последних выполненных операций отсортированных от недавних до ранних
    """
    executed_operations = []
    operations = load_operations()
    for elements in operations:
        if elements.get("state") == "EXECUTED":
            executed_operations.append(elements)
    for value in executed_operations:
        if value is None:
            executed_operations.remove(value)
    sorted_date = sorted(executed_operations, key=lambda x: x["date"], reverse=True)
    return sorted_date[:5]
