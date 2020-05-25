print("Вариант вычисления суммы и произведения комплексных чисел с использованием ООП:")
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format(self.real, sign, self.imag)
    __repr__ = __str__
class ComplexCalc:
    @staticmethod
    def add(c1, c2):
        real = c1.real + c2.real
        imag = c1.imag + c2.imag
        return Complex(real, imag)

    @staticmethod
    def mul(c1, c2):
        real = c1.real * c2.real - c1.imag * c2.imag
        imag = c1.imag * c2.real + c1.real * c2.imag
        return Complex(real, imag)




calc = ComplexCalc()
print("\nПодвариант - через прямое указание комплексного числа вида 'Complex(1, 2)': ")
print("Результат сложения:")
print(calc.add(Complex(1, 2), Complex(3, 4)))
print("Результат умножения:")
print(calc.mul(Complex(1, 2), Complex(3, 4)))
print("\nПодвариант - через указание ряда комплексных чисел в виде списка: 's = ('1 + 2i', '3 + 4i')': ")
s = ('1 + 2i', '3 + 4i')
print("Или через list:")
print(f"Результат сложения двух комплексных чисел {s[0]} и {s[1]} равен:", calc.add(Complex(int(s[0][0]), int(s[0][4])), Complex(int(s[1][0]), int(s[1][4]))))
print(f"Результат умножения двух комплексных чисел {s[0]} и {s[1]} равен:",calc.mul(Complex(int(s[0][0]), int(s[0][4])), Complex(int(s[1][0]), int(s[1][4]))))



print("")
print("Вариант вычисления суммы и произведения комплексных чисел без ООП:")
s = ('1 + 2i', '3 + 4i')
first_f = 0
second_f = 0
for i in s:
    number = list(i.split(' '))
# self.result = result
# print(self.number)
# print(self.number[2])
    first = int(number[0])
    first_f = first_f + first

    # print(first, type(first), first_f)
    second = int(list(number[2])[0])
    second_f = second_f + second
    # print(second, type(second), second_f)


print(f"Результат сложения двух комплексных чисел {s[0]} и {s[1]} равен {first_f} + {second_f}i")

# number = list(s.split(' '))

ac = int(s[0][0]) * int(s[1][0])
# print(ac)
bd = int(s[0][4]) * int(s[1][4])
# print(bd)
bc = int(s[0][4]) * int(s[1][0])
# print(bc)
ad = int(s[0][0]) * int(s[1][4])
# print(ad)
print(f"Результат умножения двух комплексных чисел {s[0]} и {s[1]} равен {ac - bd} + {bc + ad}i")

#  правило умножения комплексного числа:
# Определим произведение[5] комплексных чисел
# a + b i
#  и
# c + d i
# :
# ( a + b i ) ⋅ ( c + d i ) = a c + b c i + a d i + b d i 2 = ( a c + b d i 2 ) + ( b c + a d ) i = ( a c − b d ) + ( b c + a d ) i
# print(s.replace(" ", ""))
# s = second_f,'i'
# # s = ''.join(s.split())
# print(s)

# self.quantity = int(quantity)

# class Complex:
#     def __init__(self, number):
#
#         self.number = list(number.split(' '))
#         # self.result = result
#         # print(self.number)
#         # print(self.number[2])
#         self.first = int(self.number[0])
#         print(self.first, type(self.first))
#         self.second = int(list(self.number[2])[0])
#         print(self.second, type(self.second))
#         # self.quantity = int(quantity)
#
#
#
#     def __add__(self, other):
#         # self.result = Complex(self.first + other.first)
#         print(self.first)
#         return Complex(self.first + other.first)
#     def __str__ (self):
#         return f"Объект с параметрами ( {self.first} , {self.second} )"
#
#     # def __mul__(self, other):
#     #     #self.result = Cell(int(self.quantity * other.quantity))
#     #     return Cell(int(self.quantity * other.quantity))
#
# a = '6 + 7i'
# b = '3 + 4i'
#
# a_f = Complex(a)
# b_f = Complex(b)
# print(a_f + b_f)
#
#
#
# # # print(f"Представление операции сложения ячеек:\n",(a_f + b_f), "\n")
#
# #( a + b i ) + ( c + d i ) = ( a + c ) + ( b + d ) i  правило сложения комплексного числа
# #  правило умножения комплексного числа:
# # Определим произведение[5] комплексных чисел
# # a + b i
# #  и
# # c + d i
# # :
# # ( a + b i ) ⋅ ( c + d i ) = a c + b c i + a d i + b d i 2 = ( a c + b d i 2 ) + ( b c + a d ) i = ( a c − b d ) + ( b c + a d ) i
# # .
#
# # class Cell:
# #     def __init__(self, quantity):
# #         self.quantity = int(quantity)
# #         #self.result = result
# #
# #     def __str__(self):
# #         return f'  {self.quantity * "*"}'
# #
# #     def __add__(self, other):
# #         # self.result = Cell(self.quantity + other.quantity)
# #         return Cell(self.quantity + other.quantity)
# #
# #     def __sub__(self, other):
# #
# #         return Cell(int(self.quantity - other.quantity))
# #
# #         # return Cell(int(self.quantity - other.quantity))
# #
# #     def __mul__(self, other):
# #         #self.result = Cell(int(self.quantity * other.quantity))
# #         return Cell(int(self.quantity * other.quantity))
# #
# #     def __truediv__(self, other):
# #         #self.result = Cell(round(self.quantity // other.quantity))
# #         return Cell(int(self.quantity // other.quantity))
# #
# #
# #     def make_order(self, cells_in_row):
# #         row = ''
# #         for i in range(int(self.quantity / cells_in_row)):
# #             row += f'{"*" * cells_in_row}\\n'
# #         row += f'{"*" * (self.quantity % cells_in_row)}'
# #         return row
# #
# #
# # x_1 = int(input("Введите целое положительное число клеток:"))
# # x_2 = int(input("Введите второе целое положительное число клеток:"))
# # cells1 = Cell(x_1)
# # cells2 = Cell(x_2)
# # print(f"Представление первых ячеек:\n",cells1)
# # print(f"Представление вторых ячеек:\n",cells2)
# #
# # # print(f"Результат представленный по 10 звездочек:\n",cells1.make_order(10)"\n")
# # print(f"Результат представленный по 5 звездочек:\n", cells2.make_order(5), "\n")
# # print(f"Представление операции сложения ячеек:\n",(cells1 + cells2).make_order(5), "\n")
# # print(f"Представление операции вычитания ячеек:\n",(cells1 - cells2).make_order(5), "\n" if x_1 > x_2 else "Представление операции вычитания: \nневозможно отобразить! \n")
# # print(f"Представление операции умножения ячеек:\n",(cells2 * cells1).make_order(5), "\n")
# #
# # print(f"Представление операции деления ячеек:\n",(cells1 / cells2).make_order(5), "\n" if x_1 > x_2 else "Представление деления вычитания: \n невозможно отобразить! \n")