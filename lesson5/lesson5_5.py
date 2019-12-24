#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_list = [el for el in range(20, 41)]
sum = 0
sum_num_in_file = 0

#сформируем файл
try:
    f = open("lesson5_5.txt", "w")
    for num in my_list:
        sum += num #можно посчитать при записи в файл, но в данном случае задача не сводится к работе с файлами
        temp = str(num) + " "
        f.write(temp)
        #print(num)
    #print(sum) #для проверки вычислений
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f.close()

#прочитаем файл
try:
    f = open("lesson5_5.txt", "r")
    temp_list = []
    for i in f:
        line = i.split(" ")
    #print(line)
    for j in range(len(line)):
        if line[j] != "":
            sum_num_in_file += int(line[j])
    print("Сумма всех чисел в файле", sum_num_in_file)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f.close()