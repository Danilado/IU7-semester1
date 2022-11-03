"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 8

Номер 6

Найти максимальное значение в квадратной матрице над главной диагональю и
минимальное - под побочной диагональю
"""

# Ввод
n = int(input(
    'Введите размер n матрицы (int): '))
matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input(
            f'Введите {j+1}-й элемент {i+1}-й строки (int): '
        ))

print("\nИсходная матрица:")
for line in matrix:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()

# Транспонируем
for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# Вывод
print("\nТранспонированная матрица:")

for line in matrix:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()
