class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
        #self.result = result

    def __str__(self):
        return f'  {self.quantity * "*"}'

    def __add__(self, other):
        # self.result = Cell(self.quantity + other.quantity)
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):

        return Cell(int(self.quantity - other.quantity))

        # return Cell(int(self.quantity - other.quantity))

    def __mul__(self, other):
        #self.result = Cell(int(self.quantity * other.quantity))
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        #self.result = Cell(round(self.quantity // other.quantity))
        return Cell(int(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


x_1 = int(input("Введите целое положительное число клеток:"))
x_2 = int(input("Введите второе целое положительное число клеток:"))
cells1 = Cell(x_1)
cells2 = Cell(x_2)
print(f"Представление первых ячеек:\n",cells1)
print(f"Представление вторых ячеек:\n",cells2)

# print(f"Результат представленный по 10 звездочек:\n",cells1.make_order(10)"\n")
print(f"Результат представленный по 5 звездочек:\n", cells2.make_order(5), "\n")
print(f"Представление операции сложения ячеек:\n",(cells1 + cells2).make_order(5), "\n")
print(f"Представление операции вычитания ячеек:\n",(cells1 - cells2).make_order(5), "\n" if x_1 > x_2 else "Представление операции вычитания: \nневозможно отобразить! \n")
print(f"Представление операции умножения ячеек:\n",(cells2 * cells1).make_order(5), "\n")

print(f"Представление операции деления ячеек:\n",(cells1 / cells2).make_order(5), "\n" if x_1 > x_2 else "Представление деления вычитания: \n невозможно отобразить! \n")