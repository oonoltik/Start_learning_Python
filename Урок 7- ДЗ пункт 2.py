# Исполнено два враианта решения задачи:
# Первый вариант, простой :

print("Первый вариант")
class Textile :
# конструктор класса Textile
    def __init__ (self, y):
# Инициализация свойств.
        self.y = y

# создаем свойство вида продукции (пальто или костюм)
    @property
    def y (self):
        return self.__y
# сеттер для создания свойств
    @y.setter
    def y (self, y):
        if y == 1 :
            x = y / 6.5 + 0.5
            self.__y = float('{:.3f}'.format(x))

        elif y == 2 :
            x = y * 2 + 0.3
            self.__y = float('{:.3f}'.format(x))
        else :
            self.__y = "Wrong number!"
    def get_sq_meters (self):

        return f"Потрачено ткани на изготовление одного изделия: {self.y}кв.м."

g = int(input("Введите цифру '1' для пальто или '2' для костюма:"))
if g == 1:
    print("Изготавливаем пальто.")
elif g == 2:
    print("Изготавливаем костюм.")
else:
    print(" ")
a = Textile(g)
print(a.get_sq_meters())

print("\n\nВторой вариант:")

class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_c())
print(jacket.get_square_j())



# # class Clothes:
# #     def __init__(self, sq_mantel, sq_suites):
# #         self.sq_mantel = sq_mantel
# #         self.sq_suites = sq_suites
# #
# #
# #     # """ v - размер ( для пальто) и h - рост ( для костюма) .  """
# #     @property
# #     def sq_mantel(self):
# #         sq_mantel / 6.5 + 0.5
# #         return sq_mantel
# #
# #     #
# #     # """ v - размер ( для пальто) и h - рост ( для костюма) .  """
# #     # @property
# #     # def sq_suites(self):
# #     #     sq_suites = (2 * self.sq_suites + 0.3)
# #     #     return self.sq_suites
# #
# #     @property
# #     def my_method(self):
# #         return f"Сумарно расходуется ткани: {self.sq_mantel} ,{self.sq_suites}"
# #
# # a = Clothes(2, 3)
# # print(a.my_method())