"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class MyAbstractClothes(ABC):

    @abstractmethod
    def calc(self):
        pass


class MyCoat(MyAbstractClothes):

    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    # проверка на валидность введенных размеров пальто в диапазоне 38-58
    @size.setter
    def size(self, size):
        if size < 38:
            self.__size = 38
        elif size > 58:
            self.__size = 58
        else:
            self.__size = size

    def calc(self):
        return '{:.2f}'.format(self.size / 6.5 + 0.5)


class MySuit(MyAbstractClothes):

    def __init__(self, height):
        self.height = height

    @property
    def calc(self):
        return 2 * self.height + 0.3

##############------------ MAIN-------------------###############

coat = MyCoat(36)
print("Нужно ткани для пошива пальто", coat.calc())

suit = MySuit(0.5)
print("Нужно ткани для пошива костюма", suit.calc)
