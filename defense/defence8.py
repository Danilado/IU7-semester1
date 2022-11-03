"""Звягин Даниил ИУ7-13Б

Защита лабораторной работы номер 8

Удалить из матрицы все строки, содержащие нулевые элементы 
"""

n, m = map(int, input("Введите размеры n и m матрицы (int, int): ").split())

matrix = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = int(
            input(f"Введите значение {j+1}-го элемента {i+1}-й строки: "))
print()

i = 0
while i < len(matrix):
    if 0 in matrix[i]:
        matrix.pop(i)
    else:
        i += 1

if matrix:
    print("Изменённая матрица:")

    for line in matrix:
        for el in line:
            print(f'{el:.7g}', end='\t')
        print()

else:
    print("От матрицы ничего не осталось ;-;")
