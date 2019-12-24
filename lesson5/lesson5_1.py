#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open("lesson5_1.txt", 'w')
while True:
    inp_str = input ("Введите данные для записи в файл (для окончания ввода пустая строка и Enter): ")
    if (inp_str != ""):
        inp_str = inp_str + "\n"
        f.write(inp_str)
    else:
        f.close()
        break

f = open("lesson5_1.txt", 'r')
content = f.readlines()
print("В файл записано ", content)
f.seek(0)
for line in f:
    print(line)
f.close()


