class Data:
    def __init__(self, date):
        self.date = date

    def valid(self, date):
        print(f"Правильность ввода исходных данных:", self.validation(date))

    @classmethod
    def my_m(cls, date, months):
        try:
            day = list(date.split("-"))[0]
            month = list(date.split("-"))[1]
            year = list(date.split("-"))[2]
            month_w = months[int(month)-1].title()
            print(day, month_w, year)
        except:
            print("Проверьте ввод данных")

    @staticmethod
    def validation(date):
        try:
            if int(list(date.split("-"))[1]) > 12:
                return ("Исправьте месяц")
            if int(list(date.split("-"))[0]) > 31:
                return ("Исправьте число")
            if len(list(date.split("-"))[2]) > 4:
                return ("Исправьте год")
            else:
                return ("Нет замечаний")
        except:
            print("Проверьте данные")


months = ["января" , "февраля" , "марта" , "апреля" , "мая" , "июня" , "июля" , "августа" , "сентября" , "октября" , "ноября" , "декабря"]

d = input("Введите число в формате '10-02-1982':")

s = Data(d)
s.my_m(d, months)
s.valid(d)