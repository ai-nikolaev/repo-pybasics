# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("сотрудники.txt", "r", encoding="utf-8") as f_obj:
    print("Вывод сотрудников с окладом менее 20 тыс.:")
    for content in f_obj:
        a, b = content.split()
        if int(b) < 20000:
            print(f'\t{a}')
