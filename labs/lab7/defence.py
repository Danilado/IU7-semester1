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

split_regex = r'(\D|\W|[a-zA-Z]{2,}|\d{2,})'
search_regex = r'\d?([a-zA-Z]\d)*[a-zA-Z]?'

longest_sub = ''
maxlen = 0
max_index = None

for i, el in enumerate(arr):
    for substr in re.split(split_regex, el):

        regres = re.search(search_regex, substr)
        if regres is not None:
            regres = str(regres[0])
            reglen = len(regres)

            if reglen > maxlen:
                maxlen = reglen
                max_index = i
                longest_sub = regres

print("\nНаиболее длинная подходящая подстрока:")
print(f"{longest_sub}\n\nДлиной {maxlen} символов")
print(f"найдена в {max_index+1}-м элементе списка.")
