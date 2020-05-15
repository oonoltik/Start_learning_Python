start_dict = {}
f = "text_6.txt"
my_f = open(f, "r", encoding="utf-8-sig") # используем предложеный файл с кодировкой utf-8-sig или utf-8 - надо выбрать иначе появляется в первой строке символы "ufeff "
for line in my_f:
    z = list(line.split(" "))
    start_dict[z[0]]=z[1], z[2], z[3]

my_f.close()


import pathlib

path = pathlib.Path(f)
j = path.name
# print(path.name)  # text_6.txt
# print(path.stem)  # text_6

print("\nВыводим словарь из файла", j, "на экран: \n") # печать первой части - исходная таблица
for key, value in start_dict.items():
    n = str(' '.join(list(value)))
    print(key, n)

print("\n\nИтоговое количество часов по каждому предмету: \n") # Здесь только заголовок, сам расчет таблицы - ниже

my_f = open(f, "r", encoding="utf-8-sig")          # Блок вычисления второй таблицы
for line in my_f:

    s = line
    l = len(s)
    integ = []
    i = 0
    while i < len(s):
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))   # на этом этапе получили строки, содержащие только числа - очищенные от других символов

    def listsum(numList): # функция сумирования чисел в каждой строке
        theSum = 0
        for i in numList:
            theSum = theSum + i
        return theSum


    z = list(line.split(" "))
    start_dict[z[0]] = z[1], z[2], z[3] # опять возвращаем из каждой строки название предмета (первый элемент)

    print(z[0], listsum(integ)) # распечатываем саму вторую таблицу Предмет - Сумма часов на предмет
my_f.close()