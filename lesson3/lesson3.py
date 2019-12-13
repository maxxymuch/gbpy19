#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division (a, b):
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return 'Введена строка'
    try:
        return a / b
    except ZeroDivisionError:
        return 'Деление на ноль'


#вариант с последовательным вводом чисел в две переменных
while 1:
        first_num = input('Введите первое число (числитель), или "q" для выхода: ')
        first_num = ' '.join(first_num.split())
        if (first_num == "q"):
            break
        second_num = input ('Введите второе число (знаменатель): ')
        second_num = ' '.join(second_num.split())
        if (first_num == "" or second_num == "") or (first_num == " " or second_num == " "):
            print('\33[43m', 'Предупреждение', '\33[0m','Вы не ввели значений или ввели пробел')
        else:
            result = my_division(first_num, second_num)
            if isinstance(result, float): #проверяем результат от деления на float, потому как результат от деления float
                print ('\33[42m','Результат деления', '\33[0m', first_num, "на", second_num, "равно", '\33[42m', result, '\33[0m')
            else:
                print('\33[101m', 'Ошибка', '\033[0m', result)


#вариант с последовательным вводом чисел в список

while 1:
    string = input ('Введите последовательно два числа или "q" для выхода: ' )
    string = ' '.join(string.split()) #удаляем дублирующие пробелы
    string = string.split(" ")
    if string[0] == "q":
        break
    elif (string[0] == "" or string[1] == "") or (string[0] == " " or string[1] == " "):
        print('\33[43m', 'Предупреждение', '\33[0m', 'Вы не ввели значений или ввели пробел')
    else:
        result = my_division(string[0], string[1])
        if isinstance(result, float):  # проверяем результат от деления на float, потому как результат от деления float
            print('\33[42m', 'Результат деления', '\33[0m', string[0], "на", string[1], "равно", '\33[42m', result,
                  '\33[0m')
        else:
            print('\33[101m', 'Ошибка', '\033[0m', result)

print ("-"*100)
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

personal_id = 1
data_list = []


def personal_data(id, firstname, surname, date_of_birth, city, email, cell):
    global data_list
    data_list.append((id, {"Имя": firstname, "Фамилия": surname, "Год рождения": date_of_birth,
                           "Город": city, "Почта": email, "Телефон": cell}))
    print("Вы ввели данные", data_list)
    id += 1


while 1:  # в цикле будет только ввод данных о пользователе
    firstname = input('\nВведите имя: ')
    if (firstname == "" or firstname == "q"):  # отслеживаем выход только на вводе
        print("Ввод данных закончен")
        break

    # TODO если останется время - реализовать обязательные поля к заполнению

    surname = input('Введите фамилию: ')
    date_of_birth = input('Введите дату рожжения: ')
    city = input('Введите город: ')
    email = input('Введите эл.почту: ')
    cell = input('Введите сотовый телефон: ')
    personal_data(personal_id, firstname, surname, date_of_birth, city, email, cell)
    personal_id += 1

if (data_list):
    print("Распечатка данных")
    new_couple = ""
    for id, data in data_list:
        print('ID', id)
        for k, v in data.items():
            new_couple += v  # вывожу одни значения без ключей, потому что так понял задание
            new_couple += " "
            new_couple.rstrip()
    print(new_couple)

else:
    print('Нечего выводить')


print ("-"*100)
#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    temp_list = [a, b, c]
    max1 = max(temp_list)
    temp_list.remove(max1)
    max2 = max(temp_list)
    return f"Сумма {max1} + {max2} = {max1 + max2}"

print (my_func(56,77,99))


print ("-"*100)
#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.

# Первый — возведение в степень с помощью оператора *.

def my_func2(x,y):
    if y == 0:
        return 1
    if y < 0:
        x = 1.0 / x
        y = -y
    return x ** y

print (my_func2(3,-3))

# Второй — более сложная реализация без оператора *, предусматривающая использование цикла.
def my_func(x, y):
    if y == 0:
        return 1
    if y < 0:
        x = 1.0 / x
        y = -y
    res = x
    for i in range(y-1):
        res *= y;
    return res;

print (my_func (3,-1))


print ("-"*100)
#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

summ_global = 0

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False
    return True

def summ_list (list):
    global summ_global
    for i in list:
        if is_number(i):
            summ_global = summ_global + float(i)
    return summ_global

while 1:
    nums_input = input('Введите строку чисел с разделителем пробел, или "q" для выхода: ')
    nums_input = ' '.join(nums_input.split())
    if "q" in nums_input:
        summ_global = summ_list(nums_input)
        print (summ_global)
        break
    summ_global = summ_list(nums_input)
    print (summ_global)


print ("-"*100)
#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func (word, cap_list = False):
    new_word = ""
    if cap_list == False:
        return str(word).capitalize()
    else:
        words = ' '.join(word.split()) #удаляем дублирующие пробелы
        words = words.split(" ")
        for i in range(len(words)):
            words[i] = words[i].capitalize()
            new_word += words[i]
            new_word += " "
        return new_word.rstrip()

print (int_func("россия"))
print (int_func("россия родина моя", True))
