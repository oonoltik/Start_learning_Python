f_obj = open('homeTask_L5_1.txt', "w")
f_obj.write("Hello, my first .txt file!\n")
f_obj.close

f_obj = open( "homeTask_L5_1.txt" , "a" )
str_list = ['stroka_1\n' , 'stroka_2\n' , 'stroka_3\n']
f_obj.writelines(str_list)
f_obj.close()

with open('homeTask_L5_1.txt') as f_obj:
    for line in f_obj:
        print(line)