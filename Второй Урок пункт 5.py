my_list = [18, 17, 7, 7, 5, 5, 3, 3, 3, 3, 2, 2]
print(f"Начальный рейтинг чисел представлен как:", my_list)

digit = int(input("Введите любое натуральное число:"))

# len_list = len(my_list)
number = 0

if digit > my_list[number]:
    my_list.insert(number, digit)
elif digit < my_list[-1]:
        my_list.append(digit)
else:
    while digit < my_list[number]:
        number = number + 1
    my_list.insert(number, digit)
print(f"Новый рейтинг чисел, с учётом Вашего числа:", my_list)


