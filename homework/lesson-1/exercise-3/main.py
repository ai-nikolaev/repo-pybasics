n = 0
while n <= 0:
    n = int(input('Пожалуйста введите целое положительное число n: '))
    if n < 0:
        print('Неверно! Число должно быть положительным!')
    elif n == 0:
        print('Неверно! Число 0 не является ни положительным, ни отрицательным числом!')
result = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(f'{n} + {n}{n} + {n}{n}{n} = {result}.')
