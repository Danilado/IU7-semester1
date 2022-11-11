"""Звягин Даниил ИУ7-13Б

Кв. матрица целочисл
после каждой строки с отриц. элем вставить удвоенную соответствующую строку
"""

n = int(input("Введите значение n - размер матрицы: "))
print()

matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = int(
            input(f"Введите значение {j+1}-го элемента {i+1}-й строки: "))

print("\nИсходная матрица:")
for line in matrix:
    for element in line:
        print(f"{element:.7g}", end='\t')
    print()

for i in range(n-1, -1, -1):
    if any(el < 0 for el in matrix[i]):
        new_line = [el * 2 for el in matrix[i]]
        matrix.insert(i+1, new_line)

print("\nИтоговая матрица:")
for line in matrix:
    for element in line:
        print(f"{element:.7g}", end='\t')
    print()
