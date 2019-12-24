# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, per_hour, bonus = argv

def payment_to_staff (a, b, c):
    try:
        payroll = int(a) * int(b) + int(c)
        return payroll
    except ValueError:
        print ("Вводите целые перементы для параметров") #вывод ошибки в консоль при несоблюдении типов

print (payment_to_staff(hours, per_hour, bonus))
