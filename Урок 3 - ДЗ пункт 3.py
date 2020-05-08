def my_func(pos_1, pos_2, pos_3):
    if pos_1 > pos_2:
        if pos_2 > pos_3:
            max_sum = pos_1 + pos_3
        else:
            max_sum = pos_1 + pos_2
    else:
        max_sum = pos_2 + pos_3
    print(f"Сумма наибольших двух аргументов", max_sum)

my_func(pos_1 = float(input("Введите первое число:")) , pos_2 = float(input("Введите второе число:"))  , pos_3 = float(input("Введите третье число:")))