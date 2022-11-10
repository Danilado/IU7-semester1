"""Звягин Даниил ИУ7-13Б
Номер 4

Найти наиболее длинную непрерывную последовательность по варианту 4
Максимальный и минимальный отрицательные элементы
"""

# Для заполнения списка
from math import inf
from random import randint

length = -1
while length < 1:
    length = int(input(
        "Введите желаюмую длину начального списка (int)\n> "
    ))
    if length < 1:
        print("Ошибка! Длина списска не может быть меньше 1")

arr = [0] * length
negative_count = 0
minneg = (1, 0)
maxneg = (-inf, 0)

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
        if arr[i] < 0:
            negative_count += 1
            if arr[i] < minneg[0]:
                minneg = (arr[i], i)
            if arr[i] > maxneg[0]:
                maxneg = (arr[i], i)
else:
    for i in range(length):
        arr[i] = int(input(
            f"Введите значение {i+1}-го элемента списка (int): "
        ))
        if arr[i] < 0:
            negative_count += 1
            if arr[i] < minneg[0]:
                minneg = (arr[i], i)
            if arr[i] > maxneg[0]:
                maxneg = (arr[i], i)

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

if negative_count < 2:
    print("Ошибка в списке нет даже двух отрицательный элементов!")
else:
    arr[minneg[1]], arr[maxneg[1]] = arr[maxneg[1]], arr[minneg[1]]

print(f"\nМаксимальный отриц. элемент: {maxneg[0]} на позиции {maxneg[1]+1}")
print(f"Минимальный отриц. элемент: {minneg[0]} на позиции {minneg[1]+1}")
print("\nИзменённый список:")
for i, el in enumerate(arr):
    print(f'{i+1:>4}-й элемент: {el:.7g}')
