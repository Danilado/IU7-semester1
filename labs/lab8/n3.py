"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 8

Номер 3
Вариант 4

Найти столбец с наибольшим количеством нулевых элементов
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

max_match = 0
max_index = 0

for i in range(n):
    # Считаем кол-во нулевых элементов в столбце
    tmp_counter = 0
    for j in range(m):
        if matrix[j][i] == 0:
            tmp_counter += 1

    # Проверяем на максимальное кол-во нулевых элементов
    if tmp_counter > max_match:
        max_match = tmp_counter
        max_index = i

# Вывод
print(
    "\nНаибольшее количество нулевых элементов " +
    f"нашлось в {max_index+1}-м стоблце"
)