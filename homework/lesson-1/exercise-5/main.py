revenue = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))
if revenue > costs:
    print('Финансовый результат работы фирмы: ПРИБЫЛЬ')
    margin = revenue - costs
    profitability = margin / revenue * 100
    print(f'Рентабельность выручки: {profitability}')
    employees = int(input('Введите численность сотрудников фирмы: '))
    margin_per_employee = margin / employees
    print(f'Прибыль фирмы в расчете на одного сотрудника: {margin_per_employee}')
else:
    print('Финансовый результат работы фирмы: УБЫТОК')