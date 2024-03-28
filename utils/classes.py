from datetime import datetime


class Operation:

    def __init__(self, date, description, amount, currency, translation_from=None, translation_to=None, ):
        self.date = date
        self.description = description
        self.translation_from = translation_from
        self.translation_to = translation_to
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return (f'Дата перевода = {self.date},\n'
                f'Описание операции = {self.description},\n'
                f'Откуда перевод = {self.translation_from},\n'
                f'Куда перевод = {self.translation_to},\n'
                f'Сумма перевода = {self.amount}\n'
                f'Вид валюты = {self.currency}'
                )

    def date_output(self):
        """
        Конвертация даты произведенной операции
        :return: дата в формате ДД.ММ.ГГ
        """
        date = self.date
        if date is not None:
            date = datetime.strptime(self.date[:10], "%Y-%m-%d")
            correct_date = date.strftime("%d.%m.%Y")
            return correct_date
        return ""

    def masked_invoice_sender(self):
        """
        Шифровка номера счета отправителся в формате ХХХХ ХХ** **** ХХХХ
        :return: зашифрованный номер счета
        """
        if self.translation_from is not None:
            card = self.translation_from.split()
            number_card = str(card[-1])
            if len(number_card) == 20:
                return " ".join(card[:-1]) + " **" + number_card[-4:]
            return ' '.join(card[:-1]) + " " + number_card[:4] + " " + number_card[4:6] + "** **** " + number_card[12:]
        return ""

    def masked_invoice_recipient(self):
        """
        Шифровка номера получателя в формате **ХХХХ
        :return: зашифрованные шесть последних цифр счета отправителя
        """
        card = self.translation_to.split()
        number_card = card[-1]
        return " ".join(card[:-1]) + " **" + number_card[-4:]

    def output_result(self):
        """
        Вывод итогового результата
        """
        return (f"{self.date_output()} {self.description}\n"
                f"{self.masked_invoice_sender()} -> {self.masked_invoice_recipient()}\n"
                f"{self.amount} {self.currency}")


