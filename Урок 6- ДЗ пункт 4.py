import time
import random
class Car:
    def __init__(self, show_speed, color, name, is_police):
        self.show_speed = show_speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def auto_go(self):
        if self.is_police == False:
            self.color = self.color
        else:
            self.color = 'полицейский' + ' ' + self.color

        self.s = random.randint(1,5)
        print(f"{self.color.title()} автомобиль {self.name} тронулся с места")
        time.sleep(self.s)
        if self.s == 1:
            self.sek = 'секунду'
        elif self.s == 5:
            self.sek = 'секунд'
        else:
            self.sek = 'секунды'
        print(f"Уже через {self.s} {self.sek} автомобиль {self.name} едет со скоростью {self.show_speed} км/ч ")


        if self.show_speed  > 60 and self.is_police == False:
            print(f"Скорость {self.show_speed} км/ч - это нарушение скоростного режима!!!")
            print(f"{self.color.title()} автомобиль {self.name} остановлен полицией!!! Гонки закончились!!!!")
        else:
            print(f"Только водитель {self.color} автомобиля {self.name} знает куда он повернет через несколько секунд... ")
            self.s = random.randint(1, 5)
            self.t = random.randint(1, 2)
            time.sleep(self.s)
            if self.s == 1:
                self.sek = 'секунду'
            elif self.s == 5:
                self.sek = 'секунд'
            else:
                self.sek = 'секунды'
            if self.t == 1:
                print(f"Через {self.s} {self.sek} автомобиль {self.name} повернул Направо")
            if self.t == 2:
                print(f"Через {self.s} {self.sek} автомобиль {self.name} повернул Налево")


    def auto_stop(self):
        self.s = random.randint(1, 3)
        time.sleep(self.s)
        if self.s == 1:
            self.sek = 'секунду'
        elif self.s == 5:
            self.sek = 'секунд'
        else:
            self.sek = 'секунды'
        print(f"Через {self.s} {self.sek} {self.color} автомобиль {self.name} остановился.\n\n")

class TownCar (Car):
    pass

class SportCar (Car):
    def auto_go(self):
        if self.is_police == False:
            self.color = self.color
        else:
            self.color = 'полицейский' + ' ' + self.color

        self.s = random.randint(1,3)
        print(f"{self.color.title()} автомобиль {self.name} тронулся с места")
        time.sleep(self.s)
        if self.s == 1:
            self.sek = 'секунду'
        elif self.s == 5:
            self.sek = 'секунд'
        else:
            self.sek = 'секунды'
        print(f"Уже через {self.s} {self.sek} автомобиль {self.name} едет со скоростью {self.show_speed} км/ч ")


        if self.show_speed  > 70 and self.is_police == False:
            print(f"Скорость {self.show_speed} км/ч - даже для SportCar это черезчур !!!")
            print(f"{self.color.title()} автомобиль {self.name} остановлен полицей!!! Гонки закончились!!!!")
        else:
            print(f"Только водитель {self.color} автомобиля {self.name} знает куда он повернет через несколько секунд... ")
            self.s = random.randint(1, 3)
            self.t = random.randint(1, 2)
            time.sleep(self.s)
            if self.s == 1:
                self.sek = 'секунду'
            elif self.s == 5:
                self.sek = 'секунд'
            else:
                self.sek = 'секунды'
            if self.t == 1:
                print(f"Через {self.s} {self.sek} автомобиль {self.name} повернул Направо")
            if self.t == 2:
                print(f"Через {self.s} {self.sek} автомобиль {self.name} повернул Налево")

    #
    # def auto_stop(self):
    #     self.s = random.randint(1, 3)
    #     time.sleep(self.s)
    #     if self.s == 1:
    #         self.sek = 'секунду'
    #     elif self.s == 5:
    #         self.sek = 'секунд'
    #     else:
    #         self.sek = 'секунды'
    #     print(f"Через {self.s} {self.sek} {self.color} автомобиль {self.name} остановился")
class WorkCar (Car):
    def auto_go(self):
        if self.is_police == False:
            self.color = self.color
        else:
            self.color = 'полицейский' + ' ' + self.color

        self.s = random.randint(1, 3)
        print(f"{self.color.title()} автомобиль {self.name} тронулся с места")
        time.sleep(self.s)
        if self.s == 1:
            self.sek = 'секунду'
        elif self.s == 5:
            self.sek = 'секунд'
        else:
            self.sek = 'секунды'
        print(f"Уже через {self.s} {self.sek} автомобиль {self.name} едет со скоростью {self.show_speed} км/ч ")

        if self.show_speed > 40 and self.is_police == False:
            print(f"Скорость {self.show_speed} км/ч - для WorkCar это запредельно и опасно для остальных!!!")
            print(f"{self.color.title()} автомобиль {self.name} остановлен полицей!!! Уборка улиц подождет!!!!")
        else:
            print(
                f"Только водитель {self.color} автомобиля {self.name} знает куда он повернет через несколько секунд для уборки улиц... ")
            self.s = random.randint(1, 3)
            self.t = random.randint(1, 2)
            time.sleep(self.s)
            if self.s == 1:
                self.sek = 'секунду'
            elif self.s == 5:
                self.sek = 'секунд'
            else:
                self.sek = 'секунды'
            if self.t == 1:
                print(f"Через {self.s} {self.sek} автомобиль {self.name} повернул Направо")
            if self.t == 2:
                print(f"Через {self.s} {self.sek} автомобиль {self.name} повернул Налево")

class PoliceCar (Car):
    pass
hs = random.randint(50, 90)
a = TownCar(hs, "зеленый", "Mazda", False)
b = a.auto_go(), a.auto_stop()

hs = random.randint(50, 90)
p = PoliceCar(hs, "черный", "Ford", True)
p_s = p.auto_go(), p.auto_stop()

answer = input("Хотите еще? да/нет:")
if answer.lower() == 'нет':
    print('До свиданья, до новых встреч на дороге!')
if answer.lower() == 'да':
    hs = random.randint(50, 110)
    a = SportCar(hs, "красный", "Ferarri", False)
    b = a.auto_go(), a.auto_stop()
else:
    print('Определиться с ответом - бывает сложно! До свиданья, до новых встреч на дороге!')

answer = input("Хотите еще? да/нет:").lower()
if answer == 'нет':
     print('До свиданья, до новых встреч на дороге!')
if answer.lower() == 'да':
    hs = random.randint(30, 50)
    a = WorkCar(hs, "синий", "Сhrysler-уборщик", False)
    b = a.auto_go(), a.auto_stop()
    print('До свиданья, до новых встреч на дороге!')
else:
    print('Определиться с ответом - бывает сложно! До свиданья, до новых встреч на дороге!')