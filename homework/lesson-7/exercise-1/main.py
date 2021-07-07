# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
# в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
# новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

class Matrix:
    
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __str__(self):
        result = ''
        for line in self.matrix:
            result += '|'
            for value in line:
                result += f' {value}'
            else:
                result += ' |\r\n'
        return result
    
    def __add__(self, other):
        result = self.matrix
        for i in range(len(self.matrix)):
           for j in range(len(other.matrix)):
               result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

my_matrix1 = Matrix([[1, 1], [1, 1]])
print(my_matrix1)

my_matrix2 = Matrix([[2, 1], [2, 1]])
print(my_matrix2)

my_matrix3 = my_matrix1 + my_matrix2
print(my_matrix3)
