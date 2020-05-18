class Worker:
    salary_dict = {"wage": 2000, "bonus": 5000}
    name = 'Felix'
    surname = 'Newman'
    position = 'Top-manger'
    _income = sum(salary_dict.values())

    def get_full_name(self):
        return Worker.name +" "+ Worker.surname




    def get_total_income(self):
        return Worker.income

class Position (Worker):
    def get_full_name(self):
        return Worker.name + " " + Worker.surname

    def get_total_income(self):
        return Worker._income


a = Position()
print(f"Полное имя сотрудника:", a.get_full_name())
print(f"Доход сотрудника с учетом премии :", a.get_total_income())