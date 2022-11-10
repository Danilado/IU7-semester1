"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 7 задание 3

Вариант 3
Поиск элемента с наибольшим числом подряд идущих цифр
"""

length = -1
while length < 1:
    length = int(input(
        "Введите желаюмую длину начального списка (int)\n> "
    ))
    if length < 1:
        print("Ошибка! Длина списка не может быть меньше 1")

arr = [0] * length

for i in range(length):
    arr[i] = input(
        f"Введите значение {i+1}-го элемента списка (str): "
    )

nums = '1234567890'

maxlen = 0
maxin = -1
start = None

for i, el in enumerate(arr):
    for j, char in enumerate(el):
        if start is None:
            if char in nums:
                start = j
        elif char not in nums:
            tmp_length = j - start
            if tmp_length > maxlen:
                maxlen = tmp_length
                maxin = i
            start = None
    if start is not None:
        tmp_length = len(el) - start
        if tmp_length > maxlen:
            maxlen = tmp_length
            maxin = i
        start = None

if maxlen == 0:
    print("\nСудя по всему, ни в одном из элементов списка нет ни единого числа")
else:
    print(f"\nЭлемент с наибольшем числом идущих подряд цифр - {maxin + 1}" +
          f"\n(длина последовательности цифр - {maxlen:.7g})")
