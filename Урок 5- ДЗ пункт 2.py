my_f = open("homeTask_L5_2.txt" , "r" )
x = 0
for line in my_f:
    x += 1
    y = len(line)
    z = len(list(line.split(" ")))
    print(f"Строка №", x, ":", line, "Количество символов в строке №",x, "составляет", y, ";"'\n', "Количество слов в строке №",x, "составляет", z,"."'\n' )


my_f.close()

print(f"Количество строк в файле равно:", x)

