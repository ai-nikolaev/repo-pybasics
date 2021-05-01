# 1. Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода
# данных свидетельствует пустая строка.

with open('my_text_file.txt', 'w') as f_obj:
    while True:
        line = input("Введите сообщение для записи в файл: ")
        if len(line) == 0 or line.isspace():
            break
        print(line, file = f_obj)
