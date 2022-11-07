"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 8

Номер 5

Найти максимальное значение в квадратной матрице над главной диагональю и
минимальное - под побочной диагональю
"""

# Ввод
n = 0
while n < 1:
    n = int(input(
        'Введите размер n матрицы (int > 1): '))

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

# Ищем ответ .-.
maxover = matrix[0][1]
minbelow = matrix[n-1][n-1]

for i in range(n):
    for j in range(i+1, n):
        maxover = max(maxover, matrix[i][j])

for i in range(n):
    for j in range(i):
        minbelow = min(minbelow, matrix[i][n-1-j])

# Вывод
print(f"\nМаксимальный элемент над главной диагональю: {maxover:.7g}")
print(f"Минимальный элемент под побочной диагональю: {minbelow:.7g}")
