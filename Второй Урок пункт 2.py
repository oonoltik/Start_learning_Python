my_list= input( "Введите список значений через пробел: " ).split(" ")
# list_stroka = stroka.split(" ")
# my_list = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, False, 45, 46]
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        my_list.insert(i, my_list[i + 1])
        my_list.pop(i+2)
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        my_list.insert(i, my_list[i + 1])
        my_list.pop(i + 2)
        i += 2
print(f"Реализован обмен значений соседних элементов:", my_list)
