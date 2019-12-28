########################################################## 1 ##########################################################
# Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from datetime import datetime


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):  # метод только извлекает число, месяц, год
        my_date = []
        day_month_year = ' '.join(day_month_year.split())  # удаляем дублирующие пробелы

        for i in day_month_year.split("-"):
            my_date.append(i)

        return f'Дата {int(my_date[0])}-{int(my_date[1])}-{int(my_date[2])}'

    @staticmethod
    def data_extract(day, month, year):  # метод проводит валидацию даты

        if 1 <= day <= 31:  # TODO import calendar, пока за данность примем что в месяце 31 день
            if 1 <= month <= 12:
                if int((datetime.now()).strftime("%Y")) >= year >= 0:
                    return f'На первый взгляд всё хорошо'
                else:
                    return f'Ошибка. Нужно проверить год'
            else:
                return f'Ошибка. Нужно проверить месяц'
        else:
            return f'Ошибка. Нужно проверить день'

    def __str__(self):
        return f'Дата {Data.extract(self.day_month_year)}'


today = Data((datetime.now()).strftime("%d-%m-%Y"))
# проверим на всяческие возможности ввода даты
print(today)
print(Data.data_extract(31, 12, 2022))
print(today.data_extract(29, 2, 2011))
print(Data.extract('31 -12 - 2019'))
print(Data.extract('31-12-2019'))
print(Data.extract('31- 12- 2019'))
print(today.extract('29-2 - 2020'))  # извлечение
print(today.data_extract(29, 2, 2020))  # проверка
print(Data.data_extract(1, 11, 2000))
