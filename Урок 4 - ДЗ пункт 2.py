import random #импортируем библиотеку random
list_one = []
i = 0
while i < 10:
    list_one.append(random.randrange(0, 1000)) #формируем спсиок из 10 случайных чисел от 0-1000
    i = i + 1

list_finish = [] #задаем финишный список
el = 0
while el < len(list_one) - 1:
    if list_one[el + 1] > list_one[el]:
        list_finish.append(list_one[el+1]) #формируем финишный список по условию задачи c Элементами исходного списка, значения которых больше предыдущего элемента:
    el = el + 1
print(f"Исходный случайный список чисел:", '\n', list_one)
print(f"Элементы исходного списка, значения которых больше предыдущего элемента:", '\n', list_finish)

# не смог разобраться , почему не работает цикл for s in list:

# for el in list:
#     if list[el+1] > list[el]:
#         print(list[el], "больше", list[el+1])
#         list_finish_1.append(list[el+1])
# print(list_finish_1)



# my_list = [el > (el - 1) in list]
# {el: el* 2 for el in range( 10 , 20 )}
# print(my_list)

# from itertools import filterfalse

# data = list(filterfalse(lambda list_one[x], list_one[x+1]: x < y, list_one))
# print(data)
#Как можно увидеть из примера, в лямбда-функции осуществляется проверка на равность нулю.
# Элементы последовательности, для которых такая проверка возвращает False,
# заносятся в новый список, после чего выдаются на экран.

#
# str_1 = "abc"
# str_2 = "d"
# str_3 = "efg"
# sets = [i+j+k for i in str_1 for j in str_2 for k in str_3]
# print(sets)

