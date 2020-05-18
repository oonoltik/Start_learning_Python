class Worker:
    def __init__(self,salary_dict, name, surname, position):
        self.salary_dict = salary_dict
        self.name = name
        self.surname = surname
        self.position = position
        self._income = sum(self.salary_dict.values())

class Position (Worker):

    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.name} {self.surname}, должность: {self.position}")

    def get_total_income(self):
        print(f"Доход сотрудника с учетом премии : {self._income}")

answer = input('Хотите ввести данные или использовать по умолчанию? да/нет').lower()
if answer == 'нет':
    s = Position({"wage": 2000, "bonus": 5000},'Felix','Newman','Top-manager')
else:
    a = input('Введите имя сотрудника').lower().title()
    b = input('Введите фамилию сотрудника').lower().title()
    c = input('Введите должность сотрудника').lower().title()
    d = input('Введите оклад сотрудника')

    if d.isdigit():
        True
    else:
        d = input('Введите сумму оклада в цифрах правильно:')


    e = input('Введите премию сотрудника')
    if e.isdigit():
        True
    else:
        e = input('Введите сумму премии в цифрах правильно:')
    s = Position({"wage": int(d), "bonus": int(e)},a,b,c)

g = s.get_full_name(), s.get_total_income()

