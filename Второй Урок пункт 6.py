goods_list = [
(1, {'название':'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название':'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
# (3, {'название':'сканер', 'цена': 2000, 'количество': 72, 'eд': 'шт.'}),
]
# Начинаем цикл заполенния базы - цикл идет до сроки 45 цикл останавливается при вводе "стоп" вместо названия товара

while True:
    goods_name = input("Введите название товара или 'стоп' для остановки заполнения базы:")
    if goods_name == "стоп":
        break
# Подцикл заполения цены товара, при вводе нецифровых значений - просит ввести число
#
    while True:
        try:
            goods_price_enter = int(input("Введите цену товара:"))
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")
    goods_price = int(goods_price_enter)
# Подцикл заполения количсетва товара, при вводе нецифровых значений - просит ввести число
#
    while True:
        try:
            goods_quantity_enter = int(input("Введите количество товара:"))
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")
    goods_quantity = int(goods_quantity_enter)
# Заполения единицы измерения товара, при вводе значения "Да" в любом регистре  - возврашает значение "шт.", при другом значении - сохраняет в базу новое значение
    goods_measure = input("Товар измеряется в штуках? Введите 'Да',если это так ")
    low = goods_measure.lower()
    if low == "да":
        goods_measure = "шт."
    else:
        goods_measure = input("Введите меру измерения ")
# Формируем новую запись словаря для данного товара
    new_good_info = {'название':goods_name,'цена': goods_price, 'количество': goods_quantity, 'eд': goods_measure}
# Формируем новую запись кортежа

    new_taple = (len(goods_list)+1, new_good_info )
# Вставляем новый кортеж в конец списка структуры данных
    goods_list.append(new_taple)
    continue
# Конец цикла заполенния базы


# задаем списки для аналитики

name_list = []
price_list = []
quantity_list = []
measure_list = []

# цикл для формирования списков Values для каждого из ключей
i = 0
while True:

    goods_name = goods_list[i][1]

    name_list_add = (goods_name.get( 'название' ))
    name_list.append(name_list_add)

    price_list_add = (goods_name.get( 'цена' ))
    price_list.append(price_list_add)

    quantity_list_add = (goods_name.get( 'количество' ))
    quantity_list.append(quantity_list_add)

    measure_list_add = (goods_name.get( 'eд' ))
    measure_list.append(measure_list_add)

    i = i + 1
    if i >= len(goods_list):
        break

# полученые списки очищаем от дубликатов значений
name_list_nodubl = list(set(name_list))
price_list_nodubl = list(set(price_list))
quantity_list_nodubl = list(set(quantity_list))
measure_list_nodubl = list(set(measure_list))

# получаем  аналитику по отдельным характеристикам
name_set = {'название': name_list_nodubl}
price_set = {'цена' : price_list_nodubl}
quantity_set = {'количество' : quantity_list_nodubl}
measure_set = {'eд' : measure_list_nodubl}

# формируем сводную  аналитику по всем характеристикам в конечное множество "analitics"
analitics = {}

analitics.update(name_set)
analitics.update(quantity_set)
analitics.update(price_set)
analitics.update(measure_set)

print(f"Сводная аналитика по структуре данных представлена здесь:", analitics)
print(f"Полная структура данных на товары представлена ниже:", goods_list)

# for goods_caracters in analitics:
#     l_device, l_port = goods_caracters
#     print(f'{l_device:20} str({l_port})')