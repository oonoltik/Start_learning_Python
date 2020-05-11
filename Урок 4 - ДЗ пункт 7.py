# генератор с помощью функции с ключевым словом yield:
z = int(input("Введите число для определения факториала:"))
def generator():
    i = 1
    fact_number = 1
    global list_fact_yield
    list_fact_yield = []
    while i < z:
        fact_number = fact_number * (i + 1)
        i += 1
        list_fact_yield.append(fact_number)
    print(f"Список элементов факториала,полученный через конструкцию 'yield':", list_fact_yield)
    print("Отдельные элементы факториала:")

    for el in list_fact_yield:
        yield el
g = generator()
print(g)
for el in g:
    print(el)

#генератор через функцию 'factorial' библиотеки 'math':
print(end='\n')
from math import factorial
n = z
print(f"Проверка через функцию 'factorial' библиотеки 'math':", factorial(n))
# n = int(input("Введите число для определения факториала:"))

#генератор с помощью функции с ключевым словом return:
def fact(z):
    i = 1
    fact_number = 1
    global list_fact
    list_fact = []
    while i < z:
        fact_number = fact_number * (i+1)
        i += 1
        list_fact.append(fact_number)
    print(list_fact)

    return fact_number, list_fact
p, y = fact(z)
print(end='\n')
print(f" Проверка через ту же функцию , но с Конструкцией 'return': факториал равен",p, '\n',"Список элементов факториала:",y)
