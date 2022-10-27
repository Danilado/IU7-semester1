"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 7 задание 4

Вариант 2
Замена всех строчных гласных английских букв на заглавные
"""

the_string = input("Введите исходную строку (str): ")

filter_letters = ['a', 'e', 'i', 'o', 'u', 'y']
replacements = []

for i, char in enumerate(the_string):
    if char in filter_letters:
        replacements.append((i, char.capitalize()))

for replacement in replacements:
    the_string = the_string[:replacement[0]] + \
        replacement[1] + the_string[replacement[0]+1:]

print("Изменённая строка:")
print(the_string)
