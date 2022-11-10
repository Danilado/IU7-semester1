"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 9

Номер 4
Задана матрица D и массив I, содержащий номера строк, для которых
необходимо определить максимальный элемент. Значения максимальных
элементов запомнить в массиве R. Определить среднее арифметическое
вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
среднее арифметическое значение.
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
        matrix[i][j] = int(input(
            f'Введите {j+1}-й элемент {i+1}-й строки (int): '
        ))

print("\nИсходная матрица:")
for line in matrix:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()

Ilen = int(input("Введите длину списка I (int > 0): "))
I = [0]*Ilen
R = [0]*Ilen

for i in range(Ilen):
    I[i] = int(input("Введите НОМЕР строки: ")) - 1

for i, index in enumerate(I):
    R[i] = max(matrix[index])

avgR = sum(R)/Ilen

print("Список I")
for i, el in enumerate(I):
    print(f'{i+1}-й элемент: {el}')
print()

print("Список R")
for i, el in enumerate(R):
    print(f'{i+1}-й элемент: {el:.7g}')
print()

print(f"Среднее значение в списке R: {avgR:.7g}")
