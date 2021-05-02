# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("text_file.txt") as f_src:
    with open("new_text_file.txt", "w", encoding="utf-8") as f_dst:
        for line in f_src:
            for k, v in my_dict.items():
                line = line.replace(k, v)
            print(line, end='', file=f_dst)
