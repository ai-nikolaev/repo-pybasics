time_in_seconds = int(input('Пожалуйста введите время в секундах: '))
while time_in_seconds < 0:
    time_in_seconds = int(input('Пожалуйста введите время в секундах: '))
    if time_in_seconds < 0:
        print('Неверно! Число должно быть положительным!')
time_in_minutes = time_in_seconds // 60
hours = time_in_minutes // 60
text_hours = f'{"0" if hours < 10 else ""}{hours}'
minutes = time_in_minutes - hours * 60
text_minutes = f'{"0" if minutes < 10 else ""}{minutes}'
seconds = time_in_seconds - hours * 60 * 60 - minutes * 60
text_seconds = f'{"0" if seconds < 10 else ""}{seconds}'
print(f'{text_hours}:{text_minutes}:{text_seconds}')
