# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# from sys import argv
# script_name, first_param, second_param, third_param = argv

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

my_list = [2, 4, 6]
new_list = [el + 10 for el in my_list]
print (new_list)

my_list = [2, 5, 4, 7, 6, 9]
new_list = [el for el in my_list if el % 2 == 0]
print (new_list)

my_dict = {el: el * 2 for el in range(10, 21)}
print (my_dict)

my_set = {el ** 3 for el in range(5, 10)}
print(my_set)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и один генератор.

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор. Задача с рейтингом - подсказка

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
# произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import random

random.randint(0, 10)
random.randrange(20, 30, 3)

generator = (param * param for param in range(5))
print (generator)

for i in generator:
    print (generator)


def generate():
    for i in (10, 20, 30):
        yield i


g = generate()

print(g)

for i in g:
    print(i)

# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.


from functools import reduce


def my_func(prev_el, el):
    return prev_el + el


print (reduce(my_func, [10, 20, 30, 40]))

from functools import partial


def my_func2(el_1, el_2):
    return el_1 ** el_2


new_my_func = partial(my_func, 2)
print (new_my_func(4))

from itertools import count
for el in count(7):
    if el > 15:
        break
    else:
        print (el)

from itertools import cycle
z = 0
for el in cycle ("ASDF"):
    if z > 8:
        break
    print(el)

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.