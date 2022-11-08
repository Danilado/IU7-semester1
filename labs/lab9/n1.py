"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 9

Номер 1
Сформировать матрицу из двух данных списков как синус суммы
элементов списков на данных координатах
"""

from math import sin


m = n = 0
# Ввод
while n < 1 or m < 1:
    m, n = map(int, input(
        'Введите размеры m и n списков D и F через пробел (int > 1, int > 1): ').split()
    )
print()

d = [0]*m
f = [0]*n

av = [0]*m
l = [0]*m

matrix = [[0]*n for _ in range(m)]

for i in range(m):
    d[i] = int(input(f"Введите {i+1}-е значение списка D: "))
print()

for i in range(n):
    f[i] = int(input(f"Введите {i+1}-е значение списка F: "))
print()

for i in range(m):
    positive_counter = 0
    for j in range(n):
        cursin = sin(d[i] + f[j])
        matrix[i][j] = cursin
        if cursin > 0:
            positive_counter += 1
            av[i] = sin(d[i] + f[j])
    if av[i] > 0:
        av[i] /= positive_counter
        av[i] = round(av[i], 7)
    else:
        av[i] = 'N/A'

for i, average in enumerate(av):
    if average != 'N/A':
        for element in matrix[i]:
            if element < average:
                l[i] += 1
    else:
        l[i] = "N/A"

formatting_piece = '\t' if all([
    (average == 'N/A') or len(f'{average:.7g}') < 8
    for average in av]) else '\t\t'

print("Результаты:")
print("Матрица" + '\t'*(n)*2 + "av" + formatting_piece + "l")
for i, line in enumerate(matrix):
    for element in line:
        print(f"{element:.7g}", end='\t')
        if len(f"{element:.7g}") < 8:
            print(end='\t')
    print(f'{av[i]}', '\t', l[i], sep='')
print()
