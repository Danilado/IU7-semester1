"""Звягин Даниил ИУ7-13Б
Защита лабораторной работы номер 6

Найти второй максимум (по величине) в списке
"""
n = int(input("Введите желаемую длину списка: "))

if n < 2:
    print("\nДлина списка не может быть меньше двух!")
    exit()

arr = [0] * n

for i in range(n):
    arr[i] = int(input(f'Введите {i+1}-й элемент списка: '))

fmax = arr[0] if arr[0] > arr[1] else arr[1]
smax = arr[0] + arr[1] - fmax

if fmax == smax:
    for i in range(2, n):
        if arr[i] > fmax:
            fmax = arr[i]
            break
        elif arr[i] < smax:
            smax = arr[i]
            break
    else:
        print(
            "\nСудя по всему, в списке нет даже двух разных элементов!" +
            "\nНайти второй максимум невозможно!"
        )
        exit()

for i in range(2, n):
    if arr[i] > fmax:
        smax = fmax
        fmax = arr[i]
    elif arr[i] > smax and arr[i] != fmax:
        smax = arr[i]

print(f"\nВторой по величине элемент списка: {smax:.7g}")
