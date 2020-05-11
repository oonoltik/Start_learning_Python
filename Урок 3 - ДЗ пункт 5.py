q = 0
theSum = 0

while q == 0:
    numList = input("Введите строку чисел, разделенных пробелом, для окончания работы введите символ 'q':").split(' ')
    q = numList.count("q")
    if q != 0:
        numList.remove("q")
    for i in numList:
        try:
            i = int(i)
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")
            continue
        theSum = theSum + i
    print(f"Промежуточный результат равен:", theSum)

print(end="\n")
print(f"Конечный результат суммирования равен:", theSum)

# try:
#     goods_price_enter = int(input("Введите цену товара:"))
#     break
# except ValueError:
#     print("Вы ввели не число. Попробуйте снова: ")
#
# Работающий один цикл суммирования:
# a = input("Введите строку чисел, разделенных пробелом:")
# numList = a.split(' ')
# print(numList)
# b = numList.count("q")
# theSum = 0
# for i in numList:
#     i = int(i)
#     theSum = theSum + i
#
# print(theSum)


# my_list = list[]
# q = 0
# theSum  = 0
# going_sum = 0
# while q == 0:
#     my_list = list[input("Введите строку чисел, разделенных пробелом:")].split(' ')
#     # my_list_num = my_list.split(' ')
#     q = my_list.count("q")
#     for i in my_list_num:
#         i = int[i]
#         theSum = theSum + i
#
# going_sum = going_sum + theSum
# print(going_sum)


# my_list = list()
# q = my_list.count("q")
# theSum  = 0
# going_sum = 0
# while q == 0:
#     my_list = list(input("Введите строку чисел, разделенных пробелом:"))
#     my_list_num = my_list.split(' ')
#     q = my_list.count("q")
#     def listsum(my_list_num):
#
#         for i in my_list:
#             i = int(i)
#             theSum = theSum + i
#         return theSum
#     going_sum = going_sum + listsum()
#
# print(going_sum)


# # while my_list.count("q"):
# #     my_list = input(@)
#
# a = "1 2 5 65 4 6 4 6"
# my_list = a.split(' ')
# b = my_list.count("q")
# if b == 0:
#     def listsum(numList):
#         theSum = 0
#         for i in numList:
#             i = int(i)
#             theSum = theSum + i
#         return theSum
#
#     going_sum = listsum(my_list)
#
#     print(going_sum)
#
#
# print(b)


#     my_list = input(@)

#вариант с циклом - доработать:
# Работающий один цикл суммирования:
# a = input("Введите строку чисел, разделенных пробелом:")
# numList = a.split(' ')
# print(numList)
# b = numList.count("q")
# theSum = 0
# for i in numList:
#     i = int(i)
#     theSum = theSum + i
#
# print(theSum)

