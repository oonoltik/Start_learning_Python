import time
seconds_1 = float(time.time())
# print(seconds_1)
import re
import string
# import unicodedata
# import io

e = 'tolstoy_voskresenie_pravilniy.txt' # вводим текст для анализа


with open(e, 'r', encoding="utf-8") as f_obj:
    document_text = f_obj.read()


# document_text = open(e, 'r')
text_string = document_text.lower()
print("Введите какой язык будет попадать под анализ")
choice = int(input("1 - русские буквы, латинские буквы, французские символы с диакритикой и немецкие символы с умлаутом\n "
               "2 - только русские буквы,\n "
               "3 - только латинские буквы\n "
               "4 - только латинские буквы + франнцузские символы с диакритикой,\n "
               "5 - только латинские буквы + немецкие символы с умлаутом\n "
               "6 - только франнцузские символы с диакритикой \n "
               "7 - только немецкие символы с умлаутом \n"
               "Выш выбор: "))
if choice == 1:
    includes_words = r'\b[0-9a-zA-Zа-яА-ЯёЁÂâÀàÇçÉéÊêÈèËëÎîÔôÛûÙùÏïÜüŸÿüÜöÖäÄß\']{3,30}\b'
    # includes_words = r'\b[0-9a-zA-Zа-яА-ЯёЁÂâÀàÇçÉéÊêÈèËëÎîÔôÛûÙùÏïÜüŸÿüÜöÖäÄß]{3,30}\b'
    # Эта строка регулярного выражения проходит через весь французский текст cirano de bergerac: (вам нужно будет удалить символы языка разметки
    #http://www.gutenberg.org/files/1256/1256-8.txt
    # ^([0-9A-Za-z\u00C0-\u017F\ ,.\;'\-()\s\:\!\?\"])+



elif choice == 2:
    includes_words = r'\b[а-яА-ЯёЁ]{3,30}\b'
elif choice == 3:
    includes_words = r'\b[a-zA-Z\']{3,30}\b'

elif choice == 4:
    includes_words = r'\b[a-zA-ZÂâÀàÇçÉéÊêÈèËëÎîÔôÛûÙùÏïÜüŸÿ\']{3,30}\b'
#     # includes_words = r'\b[0-9a-zA-ZÂâÀàÇçÉéÊêÈèËëÎîÔôÛûÙùÏïÜüŸÿ]{3,30}\b'
elif choice == 5:
    includes_words = r'\b[a-zA-ZüÜöÖäÄß]{3,30}\b'
elif choice == 6:
    includes_words = r'\b[ÂâÀàÇçÉéÊêÈèËëÎîÔôÛûÙùÏïÜüŸÿ\']{3,30}\b'
elif choice == 7:
    includes_words = r'\b[üÜöÖäÄß]{3,30}\b'
else:
    print("Вы ввели неправильный выбор!")

# includes_words = r'\b[ÂâÀàÇçÉéÊêÈèËëÎîÔôÛûÙùÏïÜüŸÿ]{3,30}\b'   франнцузские символы с диакритикой
# includes_words = r'\b[üÜöÖäÄß]{3,30}\b'   немецкие символы с умлаутом
excludes_words = r"[#…\[(%\]!:@)–.;—,* «»1234567890?„-]"
text_list = re.findall(includes_words, text_string)  # выбираем слова по указаным значениям - буквы и длина слов

# print(text_list)


# РАБОТАЮЩИЙ БЛОК В НАЧАЛЕ:
# f = open('onegin.txt', 'r')
len_start = len(text_list)  # считаем сколько элементов в стартовом списке
print(f"считаем сколько элементов в стартовом списке", len_start)
# # print(f.read(1))
# l = [word.strip() for word in f]
# text_list = list(l)

count = text_list.count('')  # считает элементы с пустым значением
print(f"Пустых значений в списке", count)


named_tuple = time.localtime()  # получаем текущее время
time_string = time.strftime("%d-%m-%Y__%H-%M-%S", named_tuple)  # преобразуем текущее время в формат "%d-%m-%Y__%H-%M-%S"
name_time_data = 'analytic_' + e + "_" + time_string + ".txt"  # задаем имя сохраняемому файлу с результатми вычсилений в формате 'analytic_' + название анализируемого фала +"_"+ дата/время+".txt"

p_00 = (f'Время начала анализа текста ' + e + ":" + time_string + '\n\n')
p_01 = (f'Лексический анализ текста в файле ' + e + time_string + '\n\n')
p_02 = (f"Заданы следующие условия:\nалгоритм Включения в анализ символов в слове: " + includes_words + ',\n' + "где в квадратных скобках указаны символы в словах Включенных в поиск, а в фигурных скобках указан диапазон длины слов." + '\n\n')
p_03 = (f"\nалгоритм Исключения из анализа символов в слове: " + excludes_words + ',\n' + "где в квадратных скобках указаны символы в словах Исключенных из поиска." + '\n\n')

p_1 = (f"Считаем сколько элементов в стартовом списке в тексте " + e + ": " + str(len_start) + '\n')  # формируем строку для записи в файл аналитики
p_2 = (f"Пустых значений в стартовом списке в тексте " + e + ": " + str(count) + '\n')  # формируем строку для записи в файл аналитики

with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write(p_00)  # записыавем данные в сформированный файл аналитики
    f_obj.write(p_01)  # записыавем данные в сформированный файл аналитики
    f_obj.write(p_02)  # записыавем данные в сформированный файл аналитики
    f_obj.write(p_03)  # записыавем данные в сформированный файл аналитики
    f_obj.write(p_1)  # записыавем данные в сформированный файл аналитики
    f_obj.write(p_2)  # записыавем данные в сформированный файл аналитики

text_list = [x for x in text_list if x]  # инструмент для удаления пустых значений из списка
len_2 = len(text_list)  # считаем сколько элементов в очищенно от пробелов  списке

differ_1 = len_start - len_2
p_3 = (f"Убрали пробелов й в стартовом списке в тексте " + e + ": " + str(differ_1) + '\n')  # формируем строку для записи в файл аналитики
print(f"Убрали пробелов", differ_1)
p_4 = (f"Элементов в стартовом списке без пробелов в тексте " + e + ": " + str(len_2) + '\n')  # формируем строку для записи в файл аналитики
print(f"сколько элементов в стартовом списке без пробелов", len_2)

with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write(p_3)  # записыавем данные в сформированный файл аналитики
    f_obj.write(p_4)  # записыавем данные в сформированный файл аналитики


i = 0
w = []
while i < len(text_list):
    s = list(text_list[i].split(" "))
    text_list[i] = s
    w = w + s  # форрмируем список с каждым словом как значеним
    i = i + 1
text_list = w  # подменяем стартовый список обработаным, теперь text_list - это список с каждым словом как значеним


# i = 0
# while i < len(text_list):
#     text_list[i] = text_list[i].lower()  # делаем весь список с маленькой буквы
#     i = i + 1


i = 0
while i < len(text_list):
    text_list[i] = re.sub(excludes_words, "", text_list[i])  # убираем из каждого значения мусорные символы
    i += 1

text_list = [x for x in text_list if x]  # инструмент для удаления пустых значений из списка
text_list.sort()  # сортируем список по алфавиту
p_5 = (f"Сколько элементов-слов в конечном очищенном списке в тексте " + e + ": " + str(len(text_list)) + '\n')   # формируем строку для записи в файл аналитики
print(f"сколько элементов-слов в конечном очищенном списке ", len(text_list), '\n')
# print(text_list)

with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write(p_5)  # записыавем данные в сформированный файл аналитики


# print(f"сколько элементов-слов в конечном списке ", len(text_list), '\n')

# ПОДСЧЕТ БУКВ - занимает много времени
list_characters = []
n = 0
while n < len(text_list):
    list_characters = list(list_characters + list(text_list[n]))  # ФОРМИРУЕМ СПИСОК ИЗ ВСЕХ БУКВ ПРОИЗВЕДЕНИЯ ПОДРЯД
    n += 1

p_6 = (f"\nОбщее количество букв в тексте " + e + ": " + str(len(list_characters)) + '\n')  # формируем строку для записи в файл аналитики
with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write(p_6)  # записыавем данные в сформированный файл аналитики

print("В тексте общее количество букв:", len(list_characters))
message = list_characters
count = {}

for character in message:        # считаем совпадения
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# print(count)

d = count
list_d = list(d.items())
list_d.sort(reverse=False, key=lambda i: i[0])
print("\n\nВсе буквы текста по алфавиту:", list_d)

p_7 = (f"Все буквы текста " + e + " по алфавиту: \n " + str(list_d) + '\n')  # формируем строку для записи в файл аналитики
with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write(p_7)  # записыавем данные в сформированный файл аналитики

d = count
list_d = list(d.items())
list_d.sort(reverse=True, key=lambda i: i[1])
print("\n\nВсе буквы текста по убыванию частотности:\n", list_d)

p_8 = (f"Все буквы текста  " + e + " по убыванию частотности:\n " + str(list_d) + '\n')  # формируем строку для записи в файл аналитики
with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write(p_8)  # записыавем данные в сформированный файл аналитики


print(end='\n')

frequency = {}  # форрмируем словарь с ключами - слова и значением - частота встечи
for word in text_list:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

# print(frequency)
frequency_list = frequency.keys()
print("Все слова по алфавиту:\n")

# print(frequency)
for words in frequency_list:
    print(words, frequency[words])

import pathlib
path = pathlib.Path(e)
j = path.name
print(f"Слованый запас (уникальных слов) {j}:", len(frequency_list))
p_9 = (f"Слованый запас (уникальных слов) " + e + ": " + str(len(frequency_list)) + '\n')  # формируем строку для записи в файл аналитики
with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write(p_9)  # записыавем данные в сформированный файл аналитики

print(end='\n')
print(end='\n')
print("Все уникальные слова отсортированные по частоте употребления:\n")
with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write("\nВсе слова отсортированные по частоте употребления:\n")  # записыавем данные в сформированный файл аналитики

d = frequency
list_d = list(d.items())
list_d.sort(reverse=True, key=lambda i: i[1])

with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    z = 1
    for i in list_d:
        print(i[0], ':', i[1])
        p_10 = (str(z) + ') ' + i[0] + ':' + str(i[1]) + '\n')
        z += 1
        f_obj.write(p_10)  # записыавем данные в сформированный файл аналитики


print("Все слова по отсортированные по алфавиту:\n")

with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f_obj.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f_obj.write("\n\nВсе слова отсортированные по алфавиту:\n\n")  # записыавем данные в сформированный файл аналитики

with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики

    list_d.sort(reverse=False, key=lambda i: i[0])
    z = 1
    for i in list_d:
        print(i[0], ':', i[1])
        p_11 = (str(z) + ') ' + i[0] + ':' + str(i[1]) + '\n')
        z += 1
        f_obj.write(p_11)  # записыавем данные в сформированный файл аналитики

named_tuple_2 = time.localtime()  # получаем текущее время
time_string_2 = time.strftime("%d-%m-%Y__%H-%M-%S", named_tuple_2)  # преобразуем текущее время в формат "%d-%m-%Y__%H-%M-%S"
p_00_2 = (f'Время окончания анализа текста ' + e + ":" + time_string_2 + '\n\n')
seconds_2 = float(time.time())
print(seconds_2)
time_spend = float('{:.3f}'.format(seconds_2 - seconds_1))
p_00_3 = (f'Общее машинное время, потраченное на анализа текста составило:' + str(time_spend) + ' секунды.\n\n')

with open(name_time_data, 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write(p_00_2)  # записыавем данные в сформированный файл аналитики
    f_obj.write(p_00_3)  # записыавем данные в сформированный файл аналитики

with open('_time_statistic.txt', 'a', encoding="utf-8") as f_obj:  # формируем файл аналитики
    f_obj.write(p_00)  # записыавем данные в сформированный файл аналитики
    f_obj.write(p_00_2)  # записыавем данные в сформированный файл аналитики
    f_obj.write(p_00_3)  # записыавем данные в сформированный файл аналитики
    f_obj.write('\n')  # записыавем данные в сформированный файл аналитики