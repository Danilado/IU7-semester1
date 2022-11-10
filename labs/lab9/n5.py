"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 9

Номер 5
Дана матрица символов. Заменить в ней все гласные английские буквы на
точки. Напечатать матрицу до и после преобразования.
"""


m = n = 0
# Ввод
while n < 1 or m < 1:
    m, n = map(int, input(
        'Введите размеры m и n матрицы через пробел (int > 1, int > 1): ').split()
    )
print()


matrix = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = input(
            f'Введите {j+1}-й элемент {i+1}-й строки (char): '
        )

print("\nИсходная матрица:")
for line in matrix:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()

filter = 'aeyuio'

for i in range(m):
    for j in range(n):
        if matrix[i][j] in filter:
            matrix[i][j] = '.'

print("\nИтоговая матрица:")
for line in matrix:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()
