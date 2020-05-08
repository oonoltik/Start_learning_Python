def devision_result ():
    # global numerator, divider
    try:
        numerator = float(input("Введите числитель: "))
        divider = float(input("Введите делитель:  "))

        while divider == 0:
            divider = float(input("Делить на '0' нельзя! Введите делитель, отличный от '0' :  "))

    except ValueError:
        return

    return round(numerator / divider, 2)

print(f"Результат деления с округлением до 2 знаков после запятой:", devision_result())

