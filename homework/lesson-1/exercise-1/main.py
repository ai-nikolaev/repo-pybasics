user_name = input('Пожалуйста введите Ваше имя: ')
user_age = int(input('Пожалуйста введите Ваш возраст: '))
print(f'Привет, {user_name}! Ваш возраст {user_age}.')
if user_age >= 18:
    print('Поздравляю! Вы совершеннолетний!')
