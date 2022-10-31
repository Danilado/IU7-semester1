"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 8

Номер 2

Переставить местами строки с наибольшим и наименьшим количеством
отрицательных элементов.
"""

# Ввод
m, n = map(int, input(
    'Введите размеры m и n матрицы через пробел (int, int): ').split()
)
matrix = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input(
            f'Введите {j+1}-й элемент {i+1}-й строки (int): '
        ))

mindex = 0
mincount = n+1
maxdex = 0
maxcount = -1

for i in range(m):
    # Считаем отрицательные элементы
    tmp_counter = 0
    for element in matrix[i]:
        if element < 0:
            tmp_counter += 1

    # Записываем
    if tmp_counter > maxcount:
        maxcount = tmp_counter
        maxdex = i
    if tmp_counter < mincount:
        mincount = tmp_counter
        mindex = i

# print(mindex, maxdex)

# Замена строк
matrix[mindex], matrix[maxdex] = matrix[maxdex], matrix[mindex]

# Вывод
print("\nИзменённая матрица:")

for line in matrix:
    for element in line:
        print(f'{element}', end='\t')
    print()
