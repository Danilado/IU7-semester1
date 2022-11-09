""" Звягин Даниил ИУ7-13Б после двух с половиной часов мучений
Лабораторная работа номер 9
Задание 2

Повернуть матрицу на 90 градусов в одну сторону, а потом в другую...

!!! Я знвю, что в циклах можно обойтись и без присваивания новых
значений i и j, но я решил сделать именно так, потому что так я
нагляднее следую своему же алгоритму из картинки в файле.
Если бы я копировал код из интернета, как многие одногруппники,
я мог бы сделать всё формулами, но какой смысл

"""


n = 0
while n < 1:
    n = int(input("Введите размер матрицы (int, >0): "))

matrix = [[0]*n for _ in range(n)]

print()
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input(f"Введите {j+1}-е значение {i+1}-й строки: "))
print()

print("Исходная матрица:")
for line in matrix:
    for el in line:
        print(f"{el:.7g}", end='\t')
    print()
print()

# сдвиг по слоям
offset = 0
while offset < n//2:
    min_index = offset
    max_index = n - offset - 1

    for pos in range(max_index-min_index):
        # первые координаты в "маленькой" матрице
        i = 0
        j = pos
        cur_el = matrix[i + min_index][j + min_index]

        # Сохраняем то, что перепишем
        storage = matrix[j + min_index][max_index]
        # Переписываем
        matrix[j + min_index][max_index] = cur_el

        # заменяем координаты
        i = j
        j = max_index
        cur_el = storage

        # Сохраняем то, что перепишем
        storage = matrix[max_index][j - i]
        # Переписываем
        matrix[max_index][j - i] = cur_el

        # Заменяем координаты
        j = j - i
        i = max_index
        cur_el = storage

        # Сохраняем то, что перепишем
        storage = matrix[j][min_index]
        # Переписываем
        matrix[j][min_index] = cur_el

        # Заменяем координаты
        i = j
        j = 0
        cur_el = storage

        # Переписываем
        matrix[min_index][max_index - i + min_index] = cur_el

    offset += 1

print("Повёрнутая на 90 по часовой стрелке матица:")
for line in matrix:
    for el in line:
        print(f"{el:.7g}", end='\t')
    print()
print()

# сдвиг по слоям
for counter in range(2):
    offset = 0
    while offset < n//2:
        min_index = offset
        max_index = n - offset - 1

        for pos in range(max_index-min_index):
            relative_max_index = max_index-min_index
            # первые координаты в "маленькой" матрице
            i = 0
            j = pos
            cur_el = matrix[i + min_index][j + min_index]

            # Сохраняем то, что перепишем
            storage = matrix[max_index - j][min_index]
            # Переписываем
            matrix[max_index - j][min_index] = cur_el

            # заменяем координаты
            i = relative_max_index - j
            j = 0
            cur_el = storage

            # Сохраняем то, что перепишем
            storage = matrix[max_index][i+min_index]
            # Переписываем
            matrix[max_index][i+min_index] = cur_el

            # Заменяем координаты
            j = i
            i = relative_max_index
            cur_el = storage

            # Сохраняем то, что перепишем
            storage = matrix[max_index - j][max_index]
            # Переписываем
            matrix[max_index - j][max_index] = cur_el

            # Заменяем координаты
            cur_el = storage

            # Переписываем
            matrix[min_index][pos+min_index] = cur_el

        offset += 1
    if counter == 0:
        print("Повёрнутая на 90 против часовой стрелки матица, если имелась в виду не исходная:")
    else:
        print("Повёрнутая на 90 против часовой стрелки исходная матица:")
    for line in matrix:
        for el in line:
            print(f"{el:.7g}", end='\t')
        print()
    print()
