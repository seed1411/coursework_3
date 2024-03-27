from datetime import datetime
class Operation:

    def __init__(self, date, description, operation_amount, translation_from=None, translation_to=None, ):
        self.date = date
        self.description = description
        self.translation_from = translation_from
        self.translation_to = translation_to
        self.operation_amount = operation_amount

    def __repr__(self):
        return (f'Дата перевода = {self.date},\n'
                f'Описание операции = {self.description},\n'
                f'Откуда перевод = {self.translation_from},\n'
                f'Куда перевод = {self.translation_to},\n'
                f'Сумма перевода, валюта = {self.operation_amount}'
                )

    def date_output(self):
        """
        Конвертация даты произведенной операции
        :return: дата в формате ДД.ММ.ГГ
        """
        date = datetime.strptime(self.date[:10], "%Y-%m-%d")
        correct_date = date.strftime("%d.%m.%Y")
        return correct_date

    def masked_card(self):
        """
        Шифровка номера карты отправителся в формате ХХХХ ХХ** **** ХХХХ
        :return: зашифрованный номер карты
        """
        card = self.translation_from[-16:]
        return card[0:4] + " " + card[4:6] + "** ****" + card[12:]




