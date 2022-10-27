"""Звягин Даниил ИУ7-13Б
Защита лабораторной работы номер 7

В списке строк найти строку с наиболее длинной 
последовательностью подряд идущих цифр и латинских букв
"""

import re

length = int(input("Введите желаемую длину списка (int): "))

arr = ['']*length

print()  # newline
for i in range(length):
    arr[i] = input(f"Введите {i+1}-й элемент списка (str): ")
print()  # newline

search_regex = r'\d?([a-zA-Z]\d)*[a-zA-Z]?'

longest_sub = ''
maxlen = 0
max_index = None

for i, el in enumerate(arr):
    if el and re.fullmatch(search_regex, el):
        reglen = len(el)

        if reglen > maxlen:
            maxlen = reglen
            max_index = i
            longest_sub = el

if max_index is None:
    print("В списке нет подходящих строк!")
else:
    print("\nНаиболее длинная подходящая строка:")
    print(f"{longest_sub}\n\nДлиной {maxlen} символов")
    print(f"является {max_index+1}-м элементом списка.")
