def check_function(start_word):
    list_check = list(start_word)

    # begining of checking
    for i in list_check:

        if ord(i) > 122 or ord(i) < 97:
            finish_word = "Проверьте правильность ввода"
            break
        else:
            finish_word = start_word.title()
    # end of checking

    return finish_word

# Если программа ограничивается проверкой одного слова, то вставляем следующие две строки и этим ограничиваемся:
# start_word = input("Введите слова МАЛЕНЬКИМИ латинскими буквами:")
# print(check_function(start_word))

# Если проверяем целое предложение, то код выглядит так:

start_sent = input("Введите предложение МАЛЕНЬКИМИ латинскими буквами, слова разделены пробелами:").split(" ")
finish_sent = []
for i in start_sent:
    finish_sent.append(check_function(i))

    if finish_sent.count("Проверьте правильность ввода") != 0:
        print("Проверьте правильность ввода")
        break
else:
    print(' '.join(finish_sent))





# правильная функция для одного слова:
    # def check_function(start_word):
    #     list_check = list(start_word)
    #
    #     # begining of checking
    #     for i in list_check:
    #
    #         if ord(i) > 122 or ord(i) < 97:
    #             # print("Ошибка")
    #             finish_word = "Проверьте правильность ввода"
    #             break
    #         else:
    #             finish_word = start_word.title()
    #     # end of checking
    #
    #     return finish_word
    #
    # start_word = input("Введите слова МАЛЕНЬКИМИ латинскими буквами:")
    # print(check_function(start_word))