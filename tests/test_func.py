from utils.func import load_operations, sorting_of_executed

operation = [{"operation_1": {"state": "EXECUTED"}}, {"operation_2": {"state": "CANCELED"}}, None]
operation_executed = []


def test_load_operations():
    assert load_operations() is not None


def test_sorting_of_executed():
    assert sorting_of_executed() is not None


