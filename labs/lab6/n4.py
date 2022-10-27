"""Звягин Даниил ИУ7-13Б
Номер 4

Найти наиболее длинную непрерывную последовательность по варианту 7
Знакочередующаяся последовательность нечётных чисел
"""

# Для заполнения списка
from random import randint

length = -1
while length < 1:
    length = int(input(
        "Введите желаюмую длину начального списка (int)\n> "
    ))
    if length < 1:
        print("Ошибка! Длина списска не может быть меньше 1")

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

maxlength = 0
waystones = (0, 0)
start = finish = -1
prevsign = None

for i, el in enumerate(arr):
    if start != -1 and (el % 2 == 0 or (prevsign == (el < 0))):
        finish = i
        if maxlength < (finish - start):
            maxlength = finish - start
            waystones = (start, finish)
        start = finish = -1
    elif start == -1 and el % 2 != 0:
        start = i
        prevsign = el < 0
    else:
        prevsign = not prevsign

if start != -1:
    finish = length
    if maxlength < (finish - start):
        maxlength = finish - start
        waystones = (start, finish)


longest_sub = arr[waystones[0]:waystones[1]]

if len(longest_sub):
    print(
        "\nНаибольшая подпоследовательность найдена на позициях" +
        f" с {waystones[0]+1} по {waystones[1]}"
    )
    for i, el in enumerate(longest_sub):
        print(f'{i+1:>4}-й элемент: {el:.7g}')
else:
    print("\nВ данном списке подходящей последовательности не нашлось...")
