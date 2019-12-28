######################################## 4 ########################################
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

######################################## 5 ########################################
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую
# структуру, например словарь.

######################################## 6 ########################################
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import ABC, abstractmethod


# формируем что-то похожее на базу данных на классах
# справочник типов оргтехники

class OfficeEquipment(ABC):

    office_eq = list()

    @abstractmethod
    def get_unit(self):
        pass

class Units:
    units = {1: 'Принтер', 2: 'Сканер', 3: 'Копир'}

    @classmethod
    def get_name(cls, type):
        cls.type = type
        for k, v in Units.units.items():
            if cls.type == k:
                return v


# допустим, что существует один склад
class Warehouse:
    database = []
    unit_balance = dict()

    @property
    def get_max_key(list_):
        return max(list_)

    @classmethod
    def initwms(cls, *args):
        i = (max(Warehouse.database))[0] + 1
        while True:
            unit_ = dict()
            unit_['Тип устройства'] = input("Выберите 1 - Принтер, 2 - Сканер, 3 - Копир : ")
            unit_['Модель устройства'] = input("Введите марку и модель : ")
            unit_['Серийный номер'] = input("Введите серийный номер : ")
            unit_['Цена'] = input("Введите цену : ")
            Warehouse.database.append((i, unit_))
            i += 1
            q = input(f'Для выхода - Q, продолжение - Enter : ')
            if q == 'Q' or q == 'q':
                print(f'Наполнение склада закончено\n', Warehouse.database, "\n" * 2)
                break
            else:
                print("На склад оприходовано: \n", Warehouse.database, "\n")

    @classmethod
    def quantity(cls, type):
        count = 0
        cls.type = type
        for el in range(len(Warehouse.database)):
            if (Warehouse.database[el][1]['Тип устройства']) == str(cls.type):
                count += 1
        Warehouse.unit_balance.update({cls.type: count})
        print("Тип ", Units.get_name(cls.type), " на складе ", Warehouse.unit_balance[cls.type], " шт.", "\n" * 2)

    @classmethod
    def reception(cls):
        print("Выберите устройство для перемещение\n")
        for el in Warehouse.database:
            print(el)
        serial = input(f'Введите серийный номер для перемещения : ')
        temp_list = Warehouse.database.copy()
        for el in range(len(temp_list)):
            if temp_list[el][1]['Серийный номер'] == serial:
                OfficeEquipment.office_eq.append(temp_list[el])
                del Warehouse.database[el]

class Printer(OfficeEquipment):
    def get_unit(self):
        return f'Кол-во принтеров в использовании в офисе {OfficeEquipment.office_eq}'

class Scanner(OfficeEquipment):
    def get_unit(self):
        return f'Кол-во сканеров в использовании в офисе {OfficeEquipment.office_eq}'

class Copier(OfficeEquipment):
    def get_unit(self):
        return f'Кол-во копиров в использовании в офисе {OfficeEquipment.office_eq}'


# инициализация склада из листа
Warehouse.database = \
    [(1, {'Тип устройства': '1', 'Модель устройства': 'hp 3110', 'Серийный номер': '498787897987', 'Цена': '21000'}),
     (2, {'Тип устройства': '1', 'Модель устройства': 'kyocera 3450', 'Серийный номер': '498769735', 'Цена': '23000'}),
     (3, {'Тип устройства': '2', 'Модель устройства': 'canon lide 110', 'Серийный номер': '343459735', 'Цена': '4000'}),
     (4, {'Тип устройства': '2', 'Модель устройства': 'hp scan jet', 'Серийный номер': '45642423674', 'Цена': '3900'}),
     (5, {'Тип устройства': '3', 'Модель устройства': 'xerox workcenter', 'Серийный номер': '45645231764', 'Цена': '3900'})]

# ручная инициализация склада через input дописывание в database
Warehouse.initwms()
# Запрос остатка с типом юнита 1 (Units.units = Принтер)
Warehouse.quantity(1)
# перемещение со склада в использование при возможности
Warehouse.reception()

printer = Printer()
print(printer.get_unit())
