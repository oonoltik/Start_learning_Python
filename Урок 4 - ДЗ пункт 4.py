import random #импортируем библиотеку random
list = []
i = 0
while i < 15:
    list.append(random.randrange(0, 20)) #формируем спсиок из 10 случайных чисел от 0-20
    i = i + 1

print(f" Первая строка - Начальный список случайный список, \n Вторая строка - элементы списка, не имеющие повторений:", '\n', list, '\n', [el for el in list if list.count(el) == 1])