a = int(input( "Введите время в секундах: " ))
h = a // 3600
m = (a % 3600) // 60
s = (a % 3600) % 60
print("Пользователь ввел значение секунд, которое соотвествует", h,":",m,":",s, "или:", h,"чч:",m,"мм:",s,"сс")


# data = [h,m,s]
# my_str = ":"

# if h > 9:
#
#     print(h)
# else: print("0",h, ":")
# print(m)
# print(s)
# print(data)
#
# print( '%s %d' % (my_str, h))
#
#
# # name = input( "Enter your name: " )
# # print( "Hello, %s!" % name)