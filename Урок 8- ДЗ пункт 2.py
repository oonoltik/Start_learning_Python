class OwnError (Exception):
    def __init__(self, num):
        self.num = num
        try:
            res = 100 / num
        except ZeroDivisionError:
            print( "На ноль делить нельзя" )
        else:
            print( f"Все хорошо. Результат =", '{:.3f}'.format(res))

a = OwnError(float(input("Введите любое, кроме '0', число: ")))

# inp_data = float(input("Введите положительное число: "))

