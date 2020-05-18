losers_list = []
salary_list = []
print('\n'"Зарплатная ведомость сотрудников:"'\n')
with open('homeTask_L5_3.txt') as f_obj:

    for line in f_obj:
        z = list(line.split(" "))
        if len(z) == 3:
            print(line)
            salary_list.append(int(z[2]))
            if int(z[2]) < 20000:
                losers_list.append(z[0])
        else:
            print(f"В этой строке некорректно представлены данные, строка не участвует в расчетах\n ")
print(f'\n', "Фамилии сотрудников, которые имеют оклад менее 20 тыс.:", '\n', losers_list)
total_sum = 0
for i in salary_list:
    total_sum = total_sum + i
average_salary = total_sum / len(salary_list)
print(f'\n', "Средняя величина дохода сотрудников составляет:", '\n',average_salary)


