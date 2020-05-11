
#формируем четных список от 100 до 1000
a = [el for el in range(100,1001) if el % 2 == 0]
print(f"Список четных чисел от 100 до 1000:",a)

#Результат вычисления произведения этих чисел через цикл
finish_result = 1
i = 1
while i < len(a) + 1:
    finish_result = finish_result * a[i - 1]
    i += 1
print(f"Результат вычисления произведения этих чисел:", finish_result)
#Результат вычисления произведения этих чисел через функцию reduce
from functools import reduce
def my_func (prev_el, el):
# prev_el - предыдущий элемент
# el - текущий элемент
    return prev_el * el
print(f"Проверка вычисления произведения через 'reduce':", reduce(my_func,a))

#Сравниваем эти дв арезультата для проверки - должно получиться 0
s = finish_result - reduce(my_func,a)
print(f"Разница двух результатов, должна равняться '0':", s)

