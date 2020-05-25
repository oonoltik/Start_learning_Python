class Warehouse:  # родительский класс
    pass
    # def __init__(self, warehouse_name):
    #     self.warehouse_name = warehouse_name

class Time:   # сервисный  класс - получаем текущее время для внсения в записи

    def current_time(self):
        import time
        self.named_tuple = time.localtime()  # получаем текущее время
        self.time_string = time.strftime("%d-%m-%Y__%H-%M-%S", self.named_tuple)
        return self.time_string

a = Time()
t = a.current_time()


import re


class Person(Warehouse):  # общий класс ПЕРСОНЫ -  данные любого человека - (см. ниже Класс  статус )
    # def __init__(self):
    #     self.p_name = p_name
    #     self.p_surname = p_surname
    #     self.p_birthday = p_birthday
    #     self.doc_name  = doc_name  # наименование документа человека (паспорт)
    #     self.doc_number = doc_number  # номер документа человека (паспорт)

# TODO: добавить функцию записи нового Person в  словарь
# import re
    # @classmethod
    def new_record (self, t):                    # № 1 основная функция - ввод нового человека в базу
        self.t = t
        # self.d = d
        print('Начинаем ввода новой персоналии!')

        self.coin = 0
        while self.coin == 0:
            self.surname_f = input("Введите фамилию:").lower().title()

            self.name_check = open("person_records.txt", "r", encoding="utf-8")
            for line in self.name_check:
                self.z = list(line.split(" "))
                self.mystr = re.sub(r"[{':]", "", self.z[0])

                if self.mystr == self.surname_f:
                    self.coin = 0
                    print("Такая фамилия есть в списке, введите иначе, например 'Иванов_1'")
                    self.surname_f = input("Введите фамилию:").lower().title()
                else:
                    self.coin = 1

            self.name_check.close()
        self.name_f = input("Введите имя:").lower().title()


        self.coin_4 = 0                     # начиаем проверку введенной даты (рождения). Не удлось успеть реализовать функцию проверки ка котдельную, вызываемую по запросу.
        self.date = input("Введите дату рождения в формате '12.05.1995':")

        while self.coin_4 == 0:

            match = re.fullmatch(r'\d\d\.\d\d\.\d\d\d\d', self.date)
            if match:

                if int(list(self.date.split("."))[1]) > 12:
                    print("Исправьте месяц")
                    self.date = input("Введите дату в формате '12.05.1995':")
                    self.coin_4 = 0
                    continue
                if int(list(self.date.split("."))[0]) > 31:
                    print("Исправьте число")
                    self.date = input("Введите дату в формате '12.05.1995':")
                    self.coin_4 = 0
                    continue
                if len(list(self.date.split("."))[2]) > 4:
                    print("Исправьте год")
                    self.date = input("Введите дату в формате '12.05.1995':")
                    self.coin_4 = 0
                    continue
                self.coin_4 = 1
                break

            else:
                self.coin_4 = 0
                self.date = input("Введите дату в формате '12.05.1995':")

        # while self.coin_1 == 0:
        #
        #     match = re.fullmatch(r'\d\d\.\d\d\.\d\d\d\d', self.bd_f)
        #     if match:
        #         self.coin_1 = 1
        #         break
        #     else:
        #         self.bd_f = input("Введите дату рождения в формате '12.05.1995':")

            # print('Нашел' if match else 'Not found')
        self.doc_name = "паспорт"
        self.num_pas_f = input("Введите номер паспорта:")

        # self.named_tuple = time.localtime()  # получаем текущее время
        # self.time_string = time.strftime("%d-%m-%Y__%H-%M-%S", self.named_tuple)
        self.person_dict = {self.surname_f : [self.name_f, self.date, self.doc_name, self.num_pas_f, self.t]}  # получаем словарик с данными и со врменем формирования записи

        f_obj = open("person_records.txt" , "a", encoding="utf-8") # записываем полученую запись в конец файла "person_records.txt" с указанием времени создания записи,
                                                                    # как последнего атрибута словарика
        f_obj.write(f'\n{str(self.person_dict)}')
        f_obj.close()
        return self.person_dict

    # @classmethod
    def person_look(self):                      # № 2 основная функция - просомтр базы с людми (персоналиями)
        print('Начинаем поиск персоналии!')
        self.f_obj = open("person_records.txt", "r", encoding="utf-8")
        for line in self.f_obj:
            print(line)

        self.f_obj.close()





class PersonStatus (Person):  # список возможных статусов  любого человека - (см. его статус - сорудника, покупателя, сотрудника контрагента и проч)
    def __init__(self, p_status):
        self.p_status = p_status


class Departments(Warehouse):  # класс Департаменты (отделы)
    # def __init__(self, dep_name):
    #     self.dep_name = dep_name

    def company_check_in(self, t):          # № 3 основная функция - ввод нового контрагента в базу
        self.t = t
        print('Начинаем ввод нового контрагента!')
        self.company_class = input("Введите статус контрагента (Покупатель, Поставщик, Перевозчик):").lower().title()

        self.company_name = input("Введите наименование контрагента (в формате 'ООО 'Ромашка' '):")
        print("Введите адрес контрагента:")
        self.coin_5 = 0
        self.company_id = input("Введите шестизначный почтовый индекс контрагента:")
        while self.coin_5 == 0:

            match = re.fullmatch(r'\d\d\d\d\d\d', self.company_id)
            if match:
                self.coin_5 = 1
                break
            else:
                self.company_id = input("Введите шестизначный почтовый индекс контрагента, используя только 6 цифр:")


        self.company_adress = input("Введите почтовый адрес контрагента:")

        self.company_email = input("Введите электронный адрес контрагента:")
        self.company_phone = input("Введите телефон контрагента:")
        self.company_contact_person = input("Введите контактное лицо для связи с контрагентом:").lower().title()



        self.company_dict = {self.company_name: [self.company_class, 'адрес', self.company_id, self.company_adress, self.company_email, self.company_phone, self.company_contact_person,
                                           self.t]}  # получаем словарик с данными и со врменем формирования записи

        self.f_obj = open("company_records.txt", "a",
                          encoding="utf-8")  # записываем полученую запись в конец файла "goods_records.txt" с указанием времени создания записи,
        # как последнего атрибута словарика
        self.f_obj.write(f'\n{str(self.company_dict)}')
        self.f_obj.close()
        return self.company_dict


    def company_look(self):                         # № 4 основная функция - просомтр базы контрагентов
        print('Начинаем просмотр всех контрагентов!')
        self.f_obj = open("company_records.txt", "r", encoding="utf-8")
        for line in self.f_obj:
            print(line)

        self.f_obj.close()







class Employee (Departments):   # должность и должностные обязанности (если его статус в классе PersonStatus == сотрудник,
                                # то одновременоо он должен быть == empl_position этого списка)
    def __init__(self, empl_position, empl_description):
        self.empl_position = empl_position
        self.empl_description = empl_description


class Goods (Warehouse):  # общий класс ТОВАРЫ (Мебель, оргтехника, канцтовары, и проч)
    # def __init__(self, goods_class):
    #     self.goods_class = goods_class

    # @classmethod
    def goods_check_in(self, t):            # № 5 основная функция - ввод нового товара в базу
        self.t = t
        print('Начинаем ввод нового товара!')
        self.goods_class = input("Введите класс товара (мебель или оргтехника или канцтовары):").lower().title()

        self.goods_name = input("Введите наименование товара (в формате 'Принтер Samsung Sw-300'):").lower().title()


        self.coin_5 = 0
        self.goods_id = input("Введите пятизначный инвентарный пятизначный номер товара :")
        while self.coin_5 == 0:

            match = re.fullmatch(r'\d\d\d\d\d', self.goods_id)
            if match:
                self.coin_5 = 1
                break
            else:
                self.goods_id = input("Введите пятизначный инвентарный пятизначный номер товара, используя только 5 цифр:")

        self.coin_4 = 0  # начиаем проверку введенной даты (рождения). Не удлось успеть реализовать функцию проверки ка котдельную, вызываемую по запросу.
        self.date = input("Введите дату покупки в формате '12.05.1995':")

        while self.coin_4 == 0:

            match = re.fullmatch(r'\d\d\.\d\d\.\d\d\d\d', self.date)
            if match:

                if int(list(self.date.split("."))[1]) > 12:
                    print("Исправьте месяц")
                    self.date = input("Введите дату в формате '12.05.1995':")
                    self.coin_4 = 0
                    continue
                if int(list(self.date.split("."))[0]) > 31:
                    print("Исправьте число")
                    self.date = input("Введите дату в формате '12.05.1995':")
                    self.coin_4 = 0
                    continue
                if len(list(self.date.split("."))[2]) > 4:
                    print("Исправьте год")
                    self.date = input("Введите дату в формате '12.05.1995':")
                    self.coin_4 = 0
                    continue
                self.coin_4 = 1
                break

            else:
                self.coin_4 = 0
                self.date = input("Введите дату в формате '12.05.1995':")



        # self.coin_4 = 0
        # self.goods_purchase_date = input("Введите дату покупки :")
        # while self.coin_4 == 0:
        #
        #     match = re.fullmatch(r'\d\d\.\d\d\.\d\d\d\d', self.goods_purchase_date)
        #     if match:
        #         self.coin_4= 1
        #         break
        #     else:
        #         self.goods_purchase_date = input("Введите дату покупки в формате '12.05.1995':")


        self.goods_qauntaty = input("Введите количество товара цифрами:")

        self.coin_5 = 0
        while self.coin_5 == 0:
            if self.goods_qauntaty.isdigit():

                self.coin_5 = 1

            else:
                self.goods_qauntaty = input("Введите количество товара ТОЛЬКО цифрами:")



        # self.named_tuple = time.localtime()  # получаем текущее время
        # time_string = time.strftime("%d-%m-%Y__%H-%M-%S", self.named_tuple)
        self.goods_dict = {self.goods_id: [self.goods_class, self.goods_name, self.date, self.goods_qauntaty, self.t]}  # получаем словарик с данными и со врменем формирования записи

        self.f_obj = open("goods_records.txt", "a", encoding="utf-8")  # записываем полученую запись в конец файла "goods_records.txt" с указанием времени создания записи,
        # как последнего атрибута словарика
        self.f_obj.write(f'\n{str(self.goods_dict)}')
        self.f_obj.close()
        return self.goods_dict

    # @classmethod            # сделать проверку ФИО материального лица по нахождению в реестре person_records.txt. Если нет - внести в базу персоналию

    def goods_give_to_person(self, t):      # № 6 основная функция - передача товар материально отвественному лицу
        self.t = t
        print('Начинаем передачу товара материально-ответственному лицу!')

        self.coin_3 = 0
        while self.coin_3 == 0:
            self.goods_id_f = input("Введите пятизначный инвентарный пятизначный номер товара из 'goods_records.txt':")

            self.id_check = open("goods_records.txt", "r", encoding="utf-8")
            for line in self.id_check:
                self.z = list(line.split(" "))
                self.mystr = re.sub(r"[{':]", "", self.z[0])

                if self.mystr == self.goods_id_f:
                    self.coin_3 = 1
                    self.id_result = line
                    print(f"Найдена запись:", self.id_result)
                    break

                else:
                    self.coin_3 = 0
            # print("Такого номера нет в 'goods_records.txt'")
            # self.goods_id_f = input("Введите пятизначный инвентарный пятизначный номер товара из 'goods_records.txt':")

            self.id_check.close()


        self.mater_person_name = input("Введите фамилию материально ответственного лица, получающего товар:").lower().title()

        # self.named_tuple = time.localtime()  # получаем текущее время
        # time_string = time.strftime("%d-%m-%Y__%H-%M-%S", self.named_tuple)
        self.movement_dict = {self.id_result: ['материальное лицо:', self.mater_person_name, self.t]}  # получаем словарик с данными и со врменем формирования записи

        self.f_obj = open("movemnet_records.txt", "a", encoding="utf-8")  # записываем полученую запись в конец файла "goods_records.txt" с указанием времени создания записи,
                                                                        # как последнего атрибута словарика
        self.f_obj.write(f'\n{str(self.movement_dict)}')
        self.f_obj.close()

        return self.movement_dict


    # @classmethod
    def goods_look(self):                # № 7 основная функция - просомтр базы товаров
        print('Начинаем просмотр всех записей о товарах на складе!')
        self.f_obj = open("goods_records.txt", "r", encoding="utf-8")
        for line in self.f_obj:
            print(line)

        self.f_obj.close()



class Office_equipment (Goods):  # Подкласс класса ТОВАРЫ: Оргтехника: (список : Калькулятор, принтеры, мониторы, компютеры, сканеры, телефоын и проч)
    def __init__(self, eq_class):
        self.eq_class = eq_class



# Не усспел разобраться как выделить функци проверки (валидации) введеной даты в отдльный класс - функцию, чтобы вызывать ее по необходимости.
#сама функия написана и работает отдельно, но при запуске в общей программе - сначала срабатывает она и запрошивает ввод даты (d = date_check())
# а как сделать иначе - в лоб не разобрлася


# # @property
# def date_check():
#     import re
#     coin_4 = 0
#     date = input("Введите дату  :")
#
#     while coin_4 == 0:
#
#         match = re.fullmatch(r'\d\d\.\d\d\.\d\d\d\d', date)
#         if match:
#
#             if int(list(self.date.split("."))[1]) > 12:
#                 print("Исправьте месяц")
#                 date = input("Введите дату в формате '12.05.1995':")
#                 coin_4 = 0
#                 continue
#             if int(list(date.split("."))[0]) > 31:
#                 print("Исправьте число")
#                 date = input("Введите дату в формате '12.05.1995':")
#                 coin_4 = 0
#                 continue
#             if len(list(date.split("."))[2]) > 4:
#                 print("Исправьте год")
#                 date = input("Введите дату в формате '12.05.1995':")
#                 coin_4 = 0
#                 continue
#             coin_4 = 1
#             break
#
#         else:
#            coin_4 = 0
#            date = input("Введите дату в формате '12.05.1995':")
#
#     return date
#
#
# d = date_check()


class GoodsName(Goods):
    def __init__(self, good_number, good_name, good_status, purchase_date, material_person):
                                                 # Подкласс Единица Товарного Учета: незваисимо от его подкласса:
                                                 # Инвентарный номер .
                                                 # А также его статус- новый (new) или б/у(Used),
                                                 # дата приобретения (для дальнейшего расчета аммортизации),  связь с поставщиком)
                                                 # А также материально отвественное лицо - за кем числится этот товар == кто то из сотрудников.
                                                 # Дата передачи товара материально-отвественносму лицу
        self.good_number = good_namber
        self.good_name = good_name
        self.good_status = good_status
        self.purchase_date = purchase_date
        self.material_person = material_person

personstatus_list = ('сотрудник', 'покупатель', 'сотрудник поставщика')
# print(personstatus_list[1])
departments_list = ('бухгалтерия', 'отдел продаж', 'склад', 'производство', 'руководство', 'отдел закупок', 'отдел маркетинга')
# print(departments_list[3])
employee_list = ('менеджер', 'старший менеджер', 'директор', 'старший директор', 'бухгалтер', 'старший бухгалтер', 'маркетолог', 'страший маркетолог', 'закупщик', 'кладовщик', 'старший кладовщик', 'токарь')
# print(employee_list[8])
goods_class_list = ('мебель', 'ортехника', 'канцтовары', 'ГСМ')
eq_class_list = ('калькулятор', 'принтер', 'монитор', 'компютер', 'сканер', 'телефон', 'ноутбук')

print("\nПрограмма СКЛАД приветствует Вас!")
print("\nКакую операцию вы хотите выполнить?")
print("Для операции с товарами наберите 1")
print("Для операции с персоналиями наберите 2")
print("Для операции с контрагентами наберите 3")


def answer_checking(a,b,c):
    coin_2 = 0
    while coin_2 == 0:
        try:
            answer_1 = int(input("\nНаберите цифру, соответствующую Вашему выбору:"))

            if answer_1 != a and answer_1 != b and answer_1 != c:
                coin_2 = 0
            else:
                coin_2 = 1
        except ValueError:
            continue
    return answer_1

q_1 = answer_checking(1,2,3)
# print("Первый запрос", q_1)


if q_1 == 1:
    print("Для оприходования товара на склад наберите 1")                           #1
    print("Для перемещения товара со склада материальному лицу наберите 2")         #2
    print("Для просмотра записи о товаре на складе наберите 3")                     #3

    route = answer_checking(1,2,3)
    # print("Значение route равно", route)


if q_1 == 2:
    print("Для ввода новой персоналии нажмите 1")                                   #4
    print("Для поиска персоналии наберите 2")                                       #5

    route = int(answer_checking(1, 2, None)) + 3
    # print("Значение route равно", route)



if q_1 == 3:
    print("Для ввода нового контрагента нажмите 1")                                 #6
    print("Для поиска контрагента наберите 2")                                      #7

    route = int(answer_checking(1, 2, None)) + 5
    # print("Значение route равно", route)


if route == 1:
    a_1 = Goods()

    print(f"В файл 'goods_records.txt' была внесена запись:", a_1.goods_check_in(t))

if route == 2:
    a_2 = Goods()

    print(f"В файл 'movements_records.txt' была внесена запись:", a_2.goods_give_to_person(t))

if route == 3:
    a_3 = Goods()

    a_3.goods_look()

if route == 4:
    a_4 = Person()
    print(f"В файл 'person_records.txt' Была внсена запись:", a_4.new_record(t))

if route == 5:
    a_3 = Person()

    a_3.person_look()

if route == 6:
    a_3 = Departments()

    print(f"В файл 'company_records.txt' Была внсена запись:", a_3.company_check_in(t))

if route == 7:
    a_3 = Departments()

    a_3.company_look()








    # import pandas
