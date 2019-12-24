#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

border = 20000
count = 0
sum = 0

try:
    with open("lesson5_3.txt", encoding='utf-8') as f:
        for line in f:
            count += 1
            line = line.split(" ")
            sum += int(line[1])
            if int(line[1]) < border:
                print(line[0], "имеет оклад", line[1])
    print("Всего сотрудников", count, "\nБуджет", sum, "\nСредняя з/п", int(sum / count))

except IOError:
    print("Произошла ошибка ввода-вывода!")