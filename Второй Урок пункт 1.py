list_lesson_two = [5, 78, False, "Lesson", 89, [56, 78, "рок-н-ролл"], 5.89, (45, 54)]
# print(list_lesson_two)
a = 1
for i in list_lesson_two:
    type_list = str(type(i)).split(" ")
    # подумать как из списка типа  ['<class', "'tuple'>"] удалить все элменты кроме самого названия - может не через str а через list
    print (f"Элемент номер {a} списка имеет тип {type_list}")
    a = a + 1
    # print(type(i))