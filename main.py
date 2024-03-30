from utils.func import sorting_of_executed
from utils.classes import Operation

for element in sorting_of_executed():
    operation = Operation(
        element["date"],
        element["description"],
        element["operationAmount"]["amount"],
        element["operationAmount"]["currency"]["name"],
        element.get('from'),
        element["to"]
    )
    print(operation.output_result() + "\n")



