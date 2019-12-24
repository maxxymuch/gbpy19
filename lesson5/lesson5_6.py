#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

dict_term = {}
term_sum = 0

try:
    with open("lesson5_6.txt", encoding='utf-8') as f:
        for line in f: #вырезаем лишние символы
            line = line.split("-")
            line = ''.join(c for c in line if c != '-')
            line = line.replace("(л)", "")
            line = line.replace(":", "")
            line = line.replace("(пр)", "")
            line = line.replace("(лаб)", "")
            line = ' '.join(line.split())
            line = line.split(" ")
            #if line[0] == "One":

            i = (len(line))-1
            while i > 0:
                term_sum += int(line[i])
                i -= 1
            dict_term.update({line[0]: term_sum})
            term_sum = 0
            #print(line)
            #print(str(term_sum))
        print(dict_term)
except IOError:
    print("Произошла ошибка ввода-вывода!")