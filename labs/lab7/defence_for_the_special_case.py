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

search_regex = r'\d{0,1}([a-zA-Z]\d)*[a-zA-Z]?'
special_case = r'\d|[a-zA-Z]'

longest_sub = ''
maxlen = 0
max_index = None

for i, el in enumerate(arr):
    if re.fullmatch(search_regex, el) or re.fullmatch(special_case, el):
        reglen = len(el)

        if reglen > maxlen:
            maxlen = reglen
            max_index = i + 1
            longest_sub = el

if not max_index:
    print("В списке нет подходящих строк!")
else:
    print("\nНаиболее длинная подходящая строка:")
    print(f"{longest_sub}\n\nДлиной {maxlen} символов")
    print(f"является {max_index}-м элементом списка.")
