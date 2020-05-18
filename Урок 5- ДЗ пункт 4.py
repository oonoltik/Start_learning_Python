f_obj = open('homeTask_L5_4.txt', "w") #создаем файл
str_list = ['One — 1\n','Two — 2\n', 'Three — 3\n', 'Four — 4'] #записываем в него исходное содержимое
f_obj.writelines(str_list)
f_obj.close()


str_list_new =[]
with open('homeTask_L5_4.txt') as f_obj: # считываем записанный файл построчно
    for line in f_obj:

        z = list(line.split(" "))# формируем список с элементами строки в виде элментов списка
        # print(z)


        if z[0] == "One": # производим замену английских числительных на русские
            z[0] = 'Один'
            str_list_new.append(z) # формируем список с экончными данными

        if z[0] == "Two":
            z[0] = 'Два'
            str_list_new.append(z)

        if z[0] == "Three":
            z[0] = 'Три'
            str_list_new.append(z)

        if z[0] == "Four":
            z[0] = 'Четыре'
            str_list_new.append(z)
print("\nПострочные данные, при этом английские числительные заменены на русские:\n")
for i in str_list_new:   #  выводим на печать данные построчно с замененными числительными
    print(i)

with open('homeTask_L5_4_new.txt', "w", encoding="utf-8") as f_obj:
    i = 0
    while i < len(str_list_new):     #f_obj = open('homeTask_L5_4_new.txt', "a", encoding="utf-8")  # открываем второй файл для записи# дописываем в конец строку за строкой с изменеными данными
        f_obj.writelines(' '.join(str_list_new[i]))
        i += 1

print("\nПострочные данные из нового файла, в котором записан новый блок строк:\n") #  проверяем запись данных в новый файл построчно
with open('homeTask_L5_4_new.txt', encoding="utf-8") as f_obj:
    for line in f_obj:
        print(line)