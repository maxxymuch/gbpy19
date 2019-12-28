########################################################## 2 ##########################################################
#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя 
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivByZero:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def div_by_zero(numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return (f"Обнаружено 'деление на ноль'")


div = DivByZero(10, 100)

print(DivByZero.div_by_zero(10, 0))
print(DivByZero.div_by_zero(10, 0.151))
print(div.div_by_zero(100, 0))