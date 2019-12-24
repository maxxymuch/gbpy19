# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

from random import randint

#решение со списком
my_list = [randint(0, 20) for el in range(10)]
print ("Исходные значения списка", my_list)
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el - 1] < my_list[el]]
print("Сортированный список: ", new_list)

#решение со словарем для записи значений индекс исходного листа : его значение
new_list = {el:my_list[el] for el in range(1, len(my_list)) if my_list[el - 1] < my_list[el]}
print("Сортированный словарь: ", new_list)
