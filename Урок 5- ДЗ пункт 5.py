f_obj = open('homeTask_L5_5.txt', "w")#создаем файл
f_obj.write('56 89 23 122 45 69') #записываем набор чисел через пробел

f_obj.close

with open('homeTask_L5_5.txt') as f_obj:
    for line in f_obj:
        print(f"Набор чисел из файла:", line)
        z = list(line.split(" ")) #формируем список со значениями
total_sum = 0
for i in z: #суммируем  значения
    total_sum = total_sum + int(i)

print(f"Сумма чисел в файле: ", total_sum)#выводим конечный результат



# Вариант с  ручным вводом чисел:
print("\nВариант с ручным вводом чисел, с интересной проверкой на ввод --\n")

f_obj = open('homeTask_L5_5_2.txt', "w") #создаем файл
f_obj.write(input("Введите набор чисел, разделенных пробелами:")) #вводим набор чисел через пробел

f_obj.close

with open('homeTask_L5_5_2.txt') as f_obj:
    for line in f_obj:
        print(f"Набор чисел из файла:", line)

        z = list(line.split(" ")) #формируем список со значениями
total_sum = 0
h = 0
for i in z: #суммируем  значения
    h +=1
    try:
        total_sum = total_sum + int(i)
    except:                                 #суммируем  значения с проверкой на некорректно введеное значение
        ValueError
        print(f"Неправильно введенное число на позиции", h, "не участвовало в расчетах") # при неврном значении печатается уведомлени

print(f"Сумма чисел в файле, участвующих в расчете: ", total_sum) #выводим конечный результат