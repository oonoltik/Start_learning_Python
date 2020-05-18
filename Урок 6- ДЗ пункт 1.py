import time
class TrafficLight:

    __color = "Начальный приватный цвет - Красный. Светофор включился:\n"

    def running (self):
        a = 0
        while a < 2:

            print("\033[31m {}" .format("красный"))
            time.sleep(7)
            print("\033[33m {}".format('желтый'))
            time.sleep(2)
            print("\033[32m {}".format('зеленый'))
            time.sleep(5)
            a +=1

        print("\033[1m\033[31m\033[44m{}\033[0m".format("Программа СВЕТОФОР закончена"))

mc = TrafficLight()
print(mc._TrafficLight__color)

a = TrafficLight()
a.running()
# print(_TrafficLight().__color)

