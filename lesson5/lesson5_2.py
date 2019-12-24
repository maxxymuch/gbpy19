#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

count = 0

f = open("lesson5_2.txt", 'r', encoding='utf-8')
content = f.readlines()
print("В файле записано ", content)
print('Строк', sum(1 for line in content))
f.seek(0)
for str in f:
    count += 1
    str = str.split(" ")
    symb_count = 0
    for i in str:
        symb_count += len(i)
    print("Длина", count, "строки:", len(str), "слов", symb_count, "символов")

f.close()