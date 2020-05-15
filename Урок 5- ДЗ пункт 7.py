start_dict = {}
f = "text_7.txt"
my_f = open(f, "r", encoding="utf-8-sig") # открываем на чтение исходный файл
for line in my_f:
    z = list(line.split(" "))                          # каждую строку представлеям как список значений
    start_dict[z[1] +" "+ z[0]] = int(z[2]) - int(z[3]) # формируем словарь, где фома собсвенности и название - это ключ, а выручка и расзоды - значения


s = 0
d = 0
for i in start_dict.values(): # подсчитываем общую сумму прибыли при  условию ее положительной величины
    if i > 0:
        s = s + i
        d = d + 1
        #

average_profit  = {'average_profit': s / d} # считаем среднюю прибыль толкьо по фирмам без убытков

final_list = [start_dict, average_profit] # формируем кончный список из двух словарей - общий список фрм с данными по прибылям/убыткаам и средняя прибыль по всем безубыточным фирмам

import pathlib # симпортируем библитеку для извлечения имени файла с расширением или без

path_1 = pathlib.Path(f) # создаем пеменнцю с именем файла
j = path_1.name
# print(path.name)  # text_6.txt
# print(path.stem)  # text_6

print(f"\nПолный список фирм из файла", j, "с прибылью и средняя величина прибыли по безубыточным фирмам:\n", final_list)

import json
with open("lesson_5_task_7.json", "w", encoding='utf-8') as write_f: # производим Сериализацию в файл .json
    # json.dump(final_list, write_f)
    json.dump(final_list, write_f, indent=2, ensure_ascii=False) # при наличии символов в кириллице необходимо доработать кодировку в представленом виде

path_2 = pathlib.Path('lesson_5_task_7.json') # создаем пеменнцю с именем файла
j_2 = path_2.name

print(f"\nЧтение данных в полученном файле", j_2,":\n")
with open("lesson_5_task_7.json", "r", encoding='utf-8') as read_f:
    for line in read_f:
        print(line)
print(f"\n\nНадеюсь, что все выполнено верно!")