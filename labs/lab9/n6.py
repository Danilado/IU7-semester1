"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 9

Номер 6
Сформировать матрицу C путём построчного перемножения матриц A и B
одинаковой размерности (элементы в i-й строке матрицы A умножаются на
соответствующие элементы в i-й строке матрицы B), потом сложить все
элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
A, B, C и массив V.
"""

m = n = 0
# Ввод
while n < 1 or m < 1:
    m, n = map(int, input(
        'Введите размеры m и n матриц через пробел (int > 1, int > 1): ').split()
    )
print()


A = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        A[i][j] = int(input(
            f'Введите {j+1}-й элемент {i+1}-й строки матрицы A (int): '
        ))
print()

B = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        B[i][j] = int(input(
            f'Введите {j+1}-й элемент {i+1}-й строки матрицы B (int): '
        ))


print("\nМатрица A:")
for line in A:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()

print("\nМатрица B:")
for line in B:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()

C = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        C[i][j] = A[i][j] * B[i][j]

print("\nМатрица С:")
for line in C:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()

V = [0]*n

C = list(zip(*C))

for i in range(n):
    V[i] = sum(C[i])

print("\nСписок V")
for i, el in enumerate(V):
    print(f'{i+1}-й элемент: {el:.7g}')
