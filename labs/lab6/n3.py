"""Звягин Даниил ИУ7-13Б
Номер 3
Найти значение K-го экстремума в списке.
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

extremums = []

for i in range(1, length - 1):
    if arr[i-1] < arr[i] > arr[i+1] or \
       arr[i-1] > arr[i] < arr[i+1]:
        extremums.append((arr[i], i))

exlen = len(extremums)

if exlen == 0:
    print("\nВ этом списке нет экстремумов (не повезло...)")
else:
    num = -1
    while num < 0 or num > exlen - 1:
        num = int(input(
            "\nВведите, номер экстремума, который нужно вывести\n> "
        ))
        num -= 1
        if num < 0:
            print("Ошибка! Номер экстремума не может быть меньше либо равен нулю!")
        elif num > exlen - 1:
            print("Ошибка! В списке нет столько экстремумов!")

    print(
        f"Экстремум {num + 1}: {extremums[num][0]}" +
        f" на позиции {extremums[num][1]+1}"
    )
