from utils.func import sorting_of_executed
from utils.classes import Operation

info = sorting_of_executed()

counter = 0

for element in info:
    operation = Operation(
        element["date"],
        element["description"],
        element["operationAmount"]["amount"],
        element["operationAmount"]["currency"]["name"],
        element.get('from'),
        element["to"]
    )
    if counter == 5:
        break
    else:
        counter += 1
        print(operation.output_result() + "\n")



