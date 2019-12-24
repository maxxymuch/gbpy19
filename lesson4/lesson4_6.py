# 6. Реализовать два небольших скрипта:
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,

min_el = int(input("Укажите начальное целое число: "))
max_el = int(input("Укажтите конечное целое число: "))

for el in count(min_el):
    if el > max_el:
        break
    else:
        print (el)

# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее
print('\n'*3)

z = 0
for el in cycle ("Миру Мир"):
    if z > max_el:
        break
    print(f'{el}')
    z += 1