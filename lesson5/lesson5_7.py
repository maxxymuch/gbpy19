# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# еобходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json
import codecs

count = 0
profit = 0
average_profit = 0
total_profit = 0
firm_dict = {}
firm_list = []

try:
    with open("lesson5_7.txt", encoding='utf-8') as f:
        for line in f:
            line = line.split(" ")
            # sum += int(line[2])
            profit = int(line[2]) - int(line[3])
            if profit > 0:
                count += 1
                total_profit += profit
                print(line[1], line[0], "доходность", str(profit))
                firm_dict.update({line[0]: profit})
            else:
                print(line[1], line[0], "убыток", str(profit))
                firm_dict.update({line[0]: profit})
        average_profit = total_profit / count
        print(f"Cредняя прибыль {average_profit:.3f}")
        firm_list.append(firm_dict)
        firm_list.append({"average_profit": average_profit})
        print(firm_list)

        with codecs.open("lesson5_7.json", "w", encoding='utf-8') as js:
            for chunk in json.JSONEncoder(ensure_ascii=False, indent=4).iterencode(firm_list):
                js.write(chunk)
            #json.dump(firm_list, js)

except IOError:
    print("Произошла ошибка ввода-вывода!")
