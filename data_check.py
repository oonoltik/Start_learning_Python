class Date_check:

    def date_check(self):
        import re

        self.coin_4 = 0
        self.date = input("Введите дату  :")

        while self.coin_4 == 0:


                match = re.fullmatch(r'\d\d\.\d\d\.\d\d\d\d', self.date)
                if match:

                    if int(list(self.date.split("."))[1]) > 12:
                        print ("Исправьте месяц")
                        self.date = input("Введите дату в формате '12.05.1995':")
                        self.coin_4 = 0
                        continue
                    if int(list(self.date.split("."))[0]) > 31:
                        print ("Исправьте число")
                        self.date = input("Введите дату в формате '12.05.1995':")
                        self.coin_4 = 0
                        continue
                    if len(list(self.date.split("."))[2]) > 4:
                        print ("Исправьте год")
                        self.date = input("Введите дату в формате '12.05.1995':")
                        self.coin_4 = 0
                        continue
                    self.coin_4 = 1
                    break

                else:
                    self.coin_4 = 0
                    self.date = input("Введите дату в формате '12.05.1995':")


        return self.date

datum = Date_check()
d = datum.date_check()
# print("Выбранная дата:", d)


class SmthElse:
    def smthelsefunc(self, dt):
        self.dt = dt
        return dt

pt = SmthElse()
print(pt.smthelsefunc(d))



# try:
#     if int(list(date.split("."))[1]) > 12:
#         return ("Исправьте месяц")
#     if int(list(date.split("."))[0]) > 31:
#         return ("Исправьте число")
#     if len(list(date.split("."))[2]) > 4:
#         return ("Исправьте год")
#     else:
#         return ("Нет замечаний")
# except:
#     print("Проверьте данные")

