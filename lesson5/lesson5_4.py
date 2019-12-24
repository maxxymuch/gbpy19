# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

out_f = open("lesson5_4_ot.txt", "w")

try:
    with open("lesson5_4.txt", encoding='utf-8') as f:
        for line in f:
            line = line.split(" - ") #сложно это решить без регулярных выражений(
            if line[0] == "One":
                temp_str = "Один" + " - " + line[1]
                out_f.write(temp_str)
            elif line[0] == "Two":
                temp_str = "Два" + " - " + line[1]
                out_f.write(temp_str)
            elif line[0] == "Three":
                temp_str = "Три" + " - " + line[1]
                out_f.write(temp_str)
            elif line[0] == "Four":
                temp_str = "Четыре" + " - " + line[1]
                out_f.write(temp_str)
            else:
                print("Неизвестная прописная цифра")
except IOError:
    print("Произошла ошибка ввода-вывода!")
