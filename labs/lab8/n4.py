"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 8

Номер 4

Переставить местами столбцы с максимальной и минимальной суммой
элементов.
"""

# Ввод
from math import fsum


m, n = map(int, input(
    'Введите размеры m и n матрицы через пробел (int, int): ').split()
)
matrix = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input(
            f'Введите {j+1}-й элемент {i+1}-й строки (int): '
        ))

# Бахаем индексы вот этих ваших столбцов, да
fsum = 0
for i in range(m):
    fsum += matrix[i][0]

maxelsum = minelsum = fsum
maxindex = minindex = 0

for i in range(1, n):
    tsum = 0
    for j in range(m):
        tsum += matrix[j][i]

    if tsum > maxelsum:
        maxelsum = tsum
        maxindex = i
    elif tsum < minelsum:
        minelsum = tsum
        minindex = i

# Свапаем эти столбцы, чтоб им пусто было
for i in range(m):
    matrix[i][minindex], matrix[i][maxindex] = \
        matrix[i][maxindex], matrix[i][minindex]

# Вывод
print("\nИзменённая матрица:")

for line in matrix:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()
