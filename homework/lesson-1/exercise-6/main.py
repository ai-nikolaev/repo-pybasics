a = int(input('Введите результат пробежки спортсмена за первый день: '))
b = int(input('Введите общий результат пробежки спортсмена: '))
day = 1
value = a
print(f'{day}-й день: {value}')
while value < b:
    value = round(value + value * 0.1, 2)
    day += 1
    print(f'{day}-й день: {value}')
print(f'На {day}-й день спортсмен достиг результата — не менее {b} км.')
