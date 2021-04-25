# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Осуществить вывод данных
# о пользователе одной строкой.

# реализация функции
def person_description(name, surname, birthday, city, email, phone):
    """
    Выводит данные о пользователе одной строкой.

    Именованные параметры:
    name -- имя пользователя
    surname -- фамилия пользователя
    birthday -- год рождения
    city -- город проживания
    email -- электронная почта
    phone -- телефон
    """
    return f'{name} {surname} {birthday} {city} {email} {phone}'


# вывод результата
print(person_description(name='Имя', surname='Фамилия',
                         birthday=2021, city='Город',
                         email='abc@abc.abc', phone='123-45-67'))
