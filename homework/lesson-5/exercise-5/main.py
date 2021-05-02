# 5. Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить ее на экран.

with open("text_file.txt", "w") as f_obj1:
    while True:
        try:
            value = int(input("Введите число: "))
            print(value, end=' ', file=f_obj1)
        except ValueError:
            print('Значение не является числом. Ввод завершается.')
            break

with open("text_file.txt") as f_obj2:
    for line in f_obj2:
        print(f'Сумма чисел в файле: {sum([int(a) for a in line.split()])}')
