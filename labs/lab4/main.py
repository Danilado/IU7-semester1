"""Звягин Даниил ИУ7-13Б

Лабораторная работа номер 4
Написать программу, которая для заданных по варианту функций выведет таблицу
значений этих функций на некотором отрезке и построит график одной из них.
"""

import math as m
eps = 1e-8


# Вводим данные
start = float(input("Введите начальное значение аргумента: "))

while True:
    finish = float(input("Введите конечное значение аргумента: "))
    if abs(finish - start) < eps:
        print(
            "Ошибка! Конечная точка не " +
            "может совпадать с начальной!"
        )
        continue
    if finish < start:
        print(
            "Ошибка! Конечная точка не " +
            "может быть меньше начальной!"
        )
        continue
    break

while True:
    step = float(input("Введите величину шага: "))
    if step > (finish - start) / 2:
        print(
            "Ошибка! Введите шаг, который будет " +
            "меньше либо равен хотя-бы половины отрезка!"
        )
        continue
    if step <= 0:
        print(
            "Ошибка! Шаг не может быть " +
            "меньше либо равен нуля"
        )
        continue
    break

# Ввели данные! Молодцы!
# :) :3 (: [: :] ^-^ .-. -_- *_* *-* :> <:
# :L XD :D :d DX :o :O ;) ;] ;-; >_< :{ :| ^0^
# Всё, собрались...

# Выводим таблицу
print("----------------------------------------")
print("| x          | y1         | y2         |")
print("----------------------------------------")

# Определяем значения ф-ии на данных значениях
# аргумента
min_y = max_y = m.exp(-start) - (start - 1)**2

# Выводим таблицу
x = start
for _ in range(int((finish - start)//step + 1)+1):
    if abs(x) <= eps:
        x = 0
    if x > finish:
        break

    # Определяем значения функций на данном х
    y1 = m.exp(-x) - (x - 1)**2
    y2 = 4.07 * x**4 + 12.7 * x**3 + 8.7 * x**2 + 10.8 * x + 18.8

    # Записываем лимиты графика на данном отрезке
    # Для построения графика
    min_y = min(min_y, y1)
    max_y = max(max_y, y1)

    # Выводим строчку
    print(f"| {x:^10.4g} | {y1:^10.4g} | {y2:^10.3g} |")
    x += step

print("----------------------------------------\n")

dashes = int(input("Введите количество засечек (4 - 8): "))
dashes = min(max(dashes, 4), 8)
dashes -= 2

"""
Ширина окошка 101 символ
Надо подумать...

отдаю 8 на аргумент с полоской, осталось 93
"""

# Сформируем шкалу y
y_line = ' ' * 8  # Отделяемя от части х
step_y = (max_y - min_y) / (dashes+1)

# 91 - свободные символы
# 6 - по 3 символа от крайних засечек
# dashes + 1 - кол во промежутков
# Вычисляю максимально возможный промежуток между засечками
max_space = m.floor((91 - 6 - 6 * dashes) / (dashes + 1))

# Формирую строку для засечек
y_line += f'{min_y:^6.3g}' + ' '*max_space

y = min_y + step_y
for _ in range(dashes):
    if abs(y) < eps:
        y = 0
    y_line += f'{y:^6.3g}' + ' '*max_space
    y += step_y

y_line += f' {max_y:^6.3g}'
print(y_line)

x = start
zero_place = None

if max_y > 0 and min_y < 0:
    offset = 0 - min_y
    ratio = offset / (max_y - min_y)
    zero_place = round(ratio * 91)

for _ in range(int((finish - start)//step + 1) + 1):
    if abs(x) <= eps:
        x = 0
    if x > finish:
        break

    target_y = m.exp(-x) - (x - 1)**2
    if abs(target_y) < eps:
        target_y = 0
    offset = target_y - min_y
    ratio = offset / (max_y - min_y)
    place = round(ratio * 91)

    if place == zero_place and target_y != 0:
        if target_y > 0:
            place += 1
        elif place != 0:
            place -= 1

    this_line = f"{x:6.3g} |" + " "*(place) + "*" + " "*(91-place)

    if zero_place is not None and zero_place != place:
        this_line = (
            this_line[0:(8+zero_place)] + '|' +
            this_line[(8+zero_place+1)::]
        )

    print(this_line)
    x += step
