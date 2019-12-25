"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""

from random import randint
import numpy as np


class Matrix:

    def __init__(self, m=3, n=3):
        self.m = m
        self.n = n
        self._my_list_in_list = []
        for i in range(m):
            my_list = [randint(0, 9) for el in range(n)]
            self._my_list_in_list.append(my_list)
        print("\nЛист листов", self._my_list_in_list, "\n")

    def __str__(self):
        return ("\n".join(str(el) for el in self._my_list_in_list))

    def __add__(self, other):
        self._my_add_list = self._my_list_in_list
        for i in range(len(self._my_list_in_list)):
            for j in range(len(self._my_list_in_list[0])):
                self._my_add_list[i][j] = self._my_list_in_list[i][j] + other._my_list_in_list[i][j]
        print("\n".join(str(el) for el in self._my_add_list))


matrix1 = Matrix(5, 5)
print(matrix1)

matrix2 = Matrix(5, 5)
print(matrix2)
print("\nСумма элементов матриц\n")
matrix1 + matrix2


##############------------ NUMPY-------------------###############333

class NuMatrix:
    def __init__(self, n):
        self.n = n
        self.a = np.array([randint(0, 9) for el in range(self.n * self.n)])
        self.a.shape = (self.n, self.n)

    def __str__(self):
        return "\nПерегруженный print\n" + str(self.a)

    def __add__(self, other):
        print ("\nСумма\n", self.a + other.a)


nu_matrix1 = NuMatrix(5)
print(nu_matrix1)
nu_matrix2 = NuMatrix(5)
print(nu_matrix2)
nu_matrix1 + nu_matrix2
