elements = [1, 'A', "ABC", 2.0, None]
print(f'Список: {elements}')
for e in elements:
    if type(e) is int:
        print(f'Тип данных элемента списка "{e}" - "{int}".')
    elif type(e) is float:
        print(f'Тип данных элемента списка "{e}" - "{float}".')
    elif type(e) is str:
        print(f'Тип данных элемента списка "{e}" - "{str}".')
    elif type(e) is None:
        print(f'Тип данных элемента списка "{e}" - "{None}".')
    else:
        print(f'Тип данных элемента списка "{e}" - "{type(e)}".')