"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 9

Номер 7
Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
срез (матрицу - фрагмент трёхмерного массива) по второму индексу (нумерация
индексов начинается с 1).
"""

m = n = t = 0
while n < 1 or m < 1 or t < 1:
    m, n, t = map(int, input(
        'Введите размеры m, n и t через пробел (int > 1, *3): ').split()
    )
print()

tdim = [[[0]*t for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        for k in range(t):
            tdim[i][j][k] = int(input(
                f"Введите значение на координатах {i}, {j}, {k} (int): "
            ))

the_index = int(input("Введите ИНДЕКС для вывода среза: "))

cut = []

for i in range(m):
    cut.append(tdim[i][the_index])

print("\nСрез:")
for line in cut:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()
