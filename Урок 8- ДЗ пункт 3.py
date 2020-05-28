class OwnError:
    def is_digit(num):
        if num.isdigit():
            return True
        else:
            try:
                float(num)
                return True
            except ValueError:
                return False

list_а = []
a = input("Введите число или 'stop' для окончания программы:")
while a != 'stop':
    b = OwnError
    x = b.is_digit(a)
    # print(x)
    if x == True:
        print("\nВы ввели число, программа добавила его в список!")
        list_а.append(a)
        print("Промежуточный список введеных Вами чисел:",list_а)
    else:
        print("Вы ввели не число, повторите ввод!")

    a = input("\nВведите число или 'stop' для окончания программы:")
print("\n\nКонечный спиок введеных Вами чисел:", list_а)


