"""Звягин Даниил ИУ7-13Б
Дана квадратная матрица, повернуть на 180
"""

n = int(input("Введите размер n матрицы: "))

matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input(
            f"Введите {j+1}-й элемент {i+1}-й строки: "
        ))

print("Исходная матрица:")
for line in matrix:
    for el in line:
        print(el, end='\t')
    print()
print()

for i in range(n // 2):
    for j in range(n):
        max_index = n-i-1
        matrix[i][j], matrix[max_index][n - 1 - j] =\
            matrix[max_index][n - 1 - j], matrix[i][j]

if n % 2 == 1:
    line_i = n//2
    for j in range(n//2):
        matrix[line_i][n-1-j], matrix[line_i][j] =\
            matrix[line_i][j], matrix[line_i][n-1-j]

print("Преобразованная матрица:")
for line in matrix:
    for el in line:
        print(el, end='\t')
    print()
print()
