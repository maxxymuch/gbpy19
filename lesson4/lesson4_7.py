# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from functools import reduce
from itertools import count

def fibo_gen (n):
    fibo_list = [el for el in range(1, n+1)]
    fibo_n = reduce(lambda x, y: x * y, fibo_list)
    yield fibo_n

for el in count(1):
    if el > 15:
        break
    else:
        for i in fibo_gen(el):
            print("Факториал ", el, " = ", i)

