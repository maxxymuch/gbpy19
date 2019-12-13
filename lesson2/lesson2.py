#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

print("Задание 1. Типы данных списка")

elements = ["строка", "число", "условие", 23, 643, -1, 2.5, 4.3, 1.1, False, [1,2,3], {"a":1,"b":2,"c":3}, (4,2,1),]
print (type(elements))
for i in elements:
    print (i, " - ", type(i))

print ("-"*100)

#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

#example letter_list = ["a", "b", "c", "d", "f", "g", "h", "i", "j"]

print("Задание 2. Обмен значений соседних элементов")

count = 1
letter_list = []

while 1:#бесконечный цикл с прерыванием по пустому вводу
    el_input = input ("Введите " + str(count) + " элемент списка (для выхода - пустое значение) ")
    letter_list.append(el_input)
    count += 1
    if el_input == "":
        letter_list.pop()
        break
print ("Список до сортировки - ", letter_list)
j = 0
for i in range(int(len(letter_list) / 2)):
    letter_list[j], letter_list[j + 1] = letter_list[j + 1], letter_list[j]
    j += 2
if len(letter_list) % 2 == 0:
    print ("Сортируем список с четным кол-ом элементов")
else:
    print ("Сортируем список с нечетным кол-ом элементов")
print ("Список после сортировки - ", letter_list)

print ("-"*100)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

print("\nЗадание 3 с решением с помощью списков")
season_list = ["зима", "весна", "лето", "осень"]

#бесконечный цикл с выходом по пустому значению для реализации задачи через списки
while 1:
    months_input = input("Введите месяц в числовом формате от 1 до 12: ")
    try:
        months_input = int(months_input)
    except ValueError:
        if months_input == "":
            break
        else:
            print("Ошибка ввода. Скорее всего, вы ввели текст или нецелое число")
            continue
    if months_input in range(1,13):
        if months_input == 1 or months_input == 2 or months_input == 12:
            print("Вы ввели " + str(months_input) + " месяц - ", season_list[0] )
        elif months_input == 3 or months_input == 4 or months_input == 5:
            print("Вы ввели " + str(months_input) + " месяц - ", season_list[1] )
        elif months_input == 6 or months_input == 7 or months_input == 8:
            print("Вы ввели " + str(months_input) + " месяц - ", season_list[2] )
        elif months_input == 9 or months_input == 10 or months_input == 11:
            print("Вы ввели " + str(months_input) + " месяц - ", season_list[3] )
    else:
        print("Неверный ввод")

print ("-"*100)
print("\nЗадание 3 с решением с помощью словарей")

seasons_dict = {"зима": (1, 2, 12), "весна": (3, 4, 5), "лето": (6, 7, 8), "осень": (9, 10, 11)}

while 1:
    months_input = input("Введите месяц в числовом формате от 1 до 12: ")
    try:
        months_input = int(months_input)
    except ValueError:
        if months_input == "":
            break
        else:
            print("Ошибка ввода. Скорее всего, вы ввели текст или нецелое число")
            continue
    if months_input in range(1,13):
        for k in seasons_dict.keys():
            if months_input in seasons_dict[k]:
                print("Вы ввели " + str(months_input) + " месяц - ", k)
    else:
        print("Неверный ввод")

print ("-"*100)
#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
print("\nЗадание 4. Работа со строками")

string_length = 10

string_input = input("Введите слова или предложение: ")
string = ' '.join(string_input.split()) #удаляем дублирующие пробелы
string = string.split(" ")

print ("Исходный список ", string)
for i in (string):
    if len(i) > string_length:
        string[string.index(i)] = i[0:10] + "..." #пометим троеточием элементы списка, урезанные по условию задания
for num, el in enumerate(string,1):
     print(f"{num}: {el}")

print ("-"*100)
#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
print("\nЗадание 5. Рейтинг")

#ДОПУСТИМ, ЧТО РЕЙТИНГ 10-БАЛЬНЫЙ

rate_list = [4,7,9,5,2,1]

while 1:
    rate_input = input("Введите новый элемент рейтинга: ")
    try:
        rate_input = int(rate_input)
    except ValueError:
        if rate_input == "":
            break #выход по пустому вводу
        else:
            print("Ошибка ввода. Скорее всего, вы ввели текст или нецелое число")
            continue
    if (rate_input > 0 and rate_input <= 10):
        max_value = max(rate_list)
        #print(max_value)
        if rate_input > max_value:
            rate_list.insert(0, rate_input)
            max_value = rate_list[0]
        elif rate_input in rate_list:
            rate_list.insert(rate_list.index(rate_input), rate_input)
        else:
            rate_list.append(rate_input)
    else:
        print("Вводите положительные значения рейтинга от 1 до 10")

print(rate_list)


#6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#Пример готовой структуры:
#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]
#Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
#Пример:
#{
#
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#
#}
print("\nЗадание 6. Товары")

goods_tupple = []
goods_dict = {"название": "", "цена": 0, "количество": 0, "eд": ""}
goods_id = 1

while 1:
    goods_list = []
    good_name = input("Введите наименование " + str(goods_id) + " товара: ")
    if good_name == "":
        break  # выход по пустому вводу наименоввания
    good_price = input("Введите цену " + str(goods_id) + " товара: ")
    good_lot = input("Введите количество " + str(goods_id) + " товара: ")  # допустим что товар только штучный
    good_measure = input("Введите ед.измерения " + str(goods_id) + " товара: ")

    goods_list = (goods_id, {"название": good_name, "цена": good_price, "количество": good_lot, "ед": good_measure})
    goods_tupple.append(goods_list)
    print("Добавили в кортеж ", goods_tupple[goods_id - 1])
    goods_id += 1

try:
    print("_" * 55)
    print("Вывод статистики\n", "_" * 55)

    stat_name = [] #объявление

    for items in goods_tupple[0][1]:
        for i in range(len(goods_tupple)):
            stat_name.append((goods_tupple[i][1][items]))
        print(f"{items}: {stat_name}")
        stat_name = [] #обнуление
except IndexError:
    print("Скорее всего нет товаров для аналитики")