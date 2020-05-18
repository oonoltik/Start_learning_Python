from sys import argv
file_path, w_hours, w_rate, bonus = argv
try:
    salary = (float(w_hours) * float(w_rate)) + float(bonus)
    print("Заработная плата сотрудика составляет:", salary, "печенек.")
    print("Цените своих сотрудников!")
except ValueError:
    print("Для расчетов принимаются числа. Введите число:")



print(end= '\n')
print("Проверка параметров:")
print("Путь до файла:",file_path)
print("Рабочих часов:",w_hours)
print("Ставка за час:",w_rate)
print("Начисленая премия:",bonus)
