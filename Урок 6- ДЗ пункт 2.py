class Road:
    def __init__(self):
        self._length = float(input("Введите длину дороги в метрах:"))
        self._width  = float(input("Введите ширину дороги в метрах:"))

    def calculate(self):

        asfalt_sum = (self._width * self._length * 25 * 5) / 1000
        print(f"Масса асфальта, необходимого для покрытия всего дорожного полотна:", asfalt_sum, "тон.")

a = Road()
p_s = a.calculate()
