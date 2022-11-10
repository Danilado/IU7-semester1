"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 9

Номер 3
Подсчитать в каждой строке матрицы D количество элементов, превышающих
суммы элементов соответствующих строк матрицы Z. Разместить эти
количества в массиве G, умножить матрицу D на максимальный элемент
массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
также массив G.
"""


m = n = 0
# Ввод
while n < 1 or m < 1:
    m, n = map(int, input(
        'Введите размеры m и n матрицы D через пробел (int > 1, int > 1): ').split()
    )
print()


D = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        D[i][j] = int(input(
            f'Введите {j+1}-й элемент {i+1}-й строки матрицы D (int): '
        ))
print()

Z = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        Z[i][j] = int(input(
            f'Введите {j+1}-й элемент {i+1}-й строки матрицы Z (int): '
        ))


print("\nМатрица Z:")
for line in Z:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()

print("\nИсходная матрица D:")
for line in D:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()

G = [0]*m

for i in range(m):
    z_i_sum = sum(Z[i])

    for element in D[i]:
        if element > z_i_sum:
            G[i] += 1

maxG = max(G)

for i in range(m):
    for j in range(n):
        D[i][j] *= maxG


print("\nИтоговая матрица D:")
for line in D:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()
print()

print("Список G")
for i, el in enumerate(G):
    print(f'{i+1}-й элемент: {el}')
