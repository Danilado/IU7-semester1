"""Звягин Даниил ИУ7-13Б
Номер 1a - Добавление элемента в список
на заданную позицию средствами языка python
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

el = int(input(
    "\nВведите значение элемента, который нужно вставить в список\n> "
))

pos = -1

while pos < 0 or pos > length:
    pos = int(input(
        "\nВведите, на какое место (не индекс) в списке нужно вставить элемент (int)\n> "
    ))
    pos -= 1
    if pos < 0:
        print("Ошибка! Позиция не может быть меньше единицы\n" +
              "(вообще может, но мы же не хотим вставлять с конца)")
    elif pos > length:
        print("Ошибка! Позиция за пределами списка (и следующего элемента)")

arr.insert(pos, el)

for i, el in enumerate(arr):
    print(f'{i+1:>4}-й элемент: {el:.7g}')
