from utils.classes import Operation
import pytest

operation = Operation("2018-09-12T21:27:25.241689", "Перевод организации", "67314.70", "руб.",
                      "Visa Platinum 1246377376343588", "Счет 14211924144426031657")
operation_1 = Operation(None, "Перевод организации", "67314.70", "руб.",
                        None, "Счет 14211924144426031657")
operation_2 = Operation(None, "Перевод организации", "67314.70", "руб.",
                        "Счет 84163357546688983493", "Счет 14211924144426031657")


def test_date_output():
    assert operation.date_output() == "12.09.2018"
    assert operation_1.date_output() == ""


def test_masked_invoice_sender():
    assert operation.masked_invoice_sender() == "Visa Platinum 1246 37** **** 3588"
    assert operation_1.masked_invoice_sender() == ""
    assert operation_2.masked_invoice_sender() == "Счет **3493"


def test_masked_invoice_recipient():
    assert operation.masked_invoice_recipient() == "Счет **1657"


def test_output_result():
    assert operation.output_result() == (f"12.09.2018 Перевод организации\n"
                                         f"Visa Platinum 1246 37** **** 3588 -> Счет **1657\n"
                                         f"67314.70 руб.")
