"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 8

Номер 1
Вариант 2

Найти строку, имеющую наибольшее количество подряд
идущих одинаковых элементов.
"""

# Ввод
m, n = map(int, input(
    'Введите размеры m и n матрицы через пробел (int, int): ').split()
)
matrix = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input(
            f'Введите {j+1}-й элемент {i+1}-й строки (int): '
        ))

# print(*matrix, sep='\n')
print("\nИсходная матрица:")
for line in matrix:
    for element in line:
        print(f'{element:.7g}', end='\t')
    print()

max_count = 0
max_index = 0
counter = 0

for i in range(m):
    # Подсчёт одинаковых подряд идущих жлементов в строке матрицы
    counter = 1
    for j in range(1, n):
        if matrix[i][j] == matrix[i][j-1]:
            counter += 1
        else:
            if counter > max_count:
                max_count = counter
                max_index = i
            counter = 0

    if counter > max_count:
        max_count = counter
        max_index = i
    #counter = 0

# Вывод
print(
    '\nМаксимальное количество подряд идущих одинаковых элементов найдено в' +
    f' {max_index+1}-й строке.'
)
