"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 7 задание 1

Вариант 2
Удалить из списка все чётные элементы, без использования вложенных
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

lindex = 0

for i, el in enumerate(arr):
    if el % 2 != 0:
        arr[lindex] = el
        lindex += 1

arr = arr[:lindex]

if len(arr) == 0:
    print("\nОт списка ничего не осталось ;-;")
else:
    print("\nИзменённый список:")
    for i, el in enumerate(arr):
        print(f'{i+1:>4}-й элемент: {el:.7g}')
