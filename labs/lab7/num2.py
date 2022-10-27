"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 7 задание 2

Вариант 4
После каждого положительного элемента целочисленного списка
добавить его удвоенное значение, без использования вложенных
циклов
"""


# Для заполнения списка
from random import randint

length = -1
while length < 1:
    length = int(input(
        "Введите желаюмую длину начального списка (int)\n> "
    ))
    if length < 1:
        print("Ошибка! Длина списка не может быть меньше 1")

arr = [0] * length
input_flag = input(
    "\nЗаполнить список случайными числами? [Y/n]\n> "
)


if input_flag in ['N', 'n']:
    input_flag = False
else:
    input_flag = True

if input_flag:
    for i in range(length):
        arr[i] = randint(-100, 100)
else:
    for i in range(length):
        arr[i] = int(input(
            f"Введите значение {i+1}-го элемента списка (int): "
        ))

out_flag = input(
    "\nВывести исходный список? [N/y]\n> "
)

if out_flag in ['N', 'n', '']:
    out_flag = False
else:
    out_flag = True

if out_flag:
    for i, el in enumerate(arr):
        print(f'{i+1:>4}-й элемент: {el:.7g}')

positive_count = 0
for el in arr:
    if el > 0:
        positive_count += 1

arr += [0]*positive_count

cur_pos = length + positive_count - 1
for i in range(length-1, -1, -1):
    if arr[i] > 0:
        arr[cur_pos] = arr[i]*2
        arr[cur_pos-1] = arr[i]
        cur_pos -= 2
    else:
        arr[cur_pos] = arr[i]
        cur_pos -= 1

print("\nИзменённый список:")
for i, el in enumerate(arr):
    print(f'{i+1:>4}-й элемент: {el:.7g}')
