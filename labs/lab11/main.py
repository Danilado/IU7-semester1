"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 11

Исслкдование методов сортировки
===============================

Метод простого выбора
a.k.a. простой перебор
-------------------------------
"""

# Самописная библиотека для ввода значений по всем правилам
import fast_inputs as fi
# Самописная библиотека для вывода списков и т.д.
import fast_outputs as fo
# Типизации навалим
from typing import List, Union
# Времечко
import time


def find_min_index(arr: List) -> int:
    """Возвращает индекс минимального элемента

    :param arr: Список
    :type arr: List
    :return: Индекс минимального элемента
    :rtype: int
    """
    min_el = arr[0]
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] < min_el:
            min_index = i
            min_el = arr[i]

    return min_index


def simple_choise_sort(arr: List) -> Union[List, int]:
    """Сортирует список методом простого выбора

    :param arr: Список для сортировки
    :type arr: List
    :return: Список и количество перестановок
    :rtype: Union[List, int]
    """
    swaps = 0

    for i in range(len(arr) - 1):
        min_index = find_min_index(arr[i::]) + i
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
            swaps += 1

    return arr, swaps


def main():
    n = fi.param_input(int, "n>0", "Введите желаемую длину списка: ")
    arr = fi.input_list(n, int)
    fo.list_output(arr, style='lab', comment="\nВведённый список:")

    times = [0]*9
    swaps = [0]*9
    ns = [0]*3

    arr, _ = simple_choise_sort(arr)

    fo.list_output(arr, style='lab', comment="\nОтсортированный список:")

    log_flag = fi.param_input(
        str,
        r'[yYnN]|(Y|yes)|(N|no)|.{0}',
        "\nВыводить списки в процессе выполнения программы? (N/y): "
    )
    log_flag = True if log_flag and log_flag in 'Yyes' else False

    for i in range(3):
        n = fi.param_input(
            int, 'n>0', f"\nВведите длину n{i+1} списка для тестирования алгоритма: ")
        ns[i] = n

        arr = [0]*n
        timestamp = time.time()
        arr = fi.rand_fill(arr)
        print(f"Список заполнялся {time.time() - timestamp:.4g}с")

        if log_flag:
            fo.list_output(arr, 'normal', comment="\nСформированный список:")

        timestamp = time.time()
        arr, swaps[i*3] = simple_choise_sort(arr)
        times[i*3] = time.time() - timestamp

        if log_flag:
            fo.list_output(arr, 'normal', comment="\nОтсортированный список:")
            print("Следующая сортировка по нему же")

        timestamp = time.time()
        arr, swaps[i*3 + 1] = simple_choise_sort(arr)
        times[i*3 + 1] = time.time() - timestamp

        if log_flag:
            fo.list_output(arr, 'normal', comment="\nОтсортированный список:")

        arr = arr[::-1]

        if log_flag:
            fo.list_output(arr, 'normal', comment="\nРазвёрнутый список:")

        timestamp = time.time()
        arr, swaps[i*3 + 2] = simple_choise_sort(arr)
        times[i*3 + 2] = time.time() - timestamp

        if log_flag:
            fo.list_output(arr, 'normal', comment="\nОтсортированный список:")

    print('-'*129)
    print(f'| Список \\ n | {ns[0]:^36} | {ns[1]:^36}| {ns[2]:^36}|')
    print('-'*129)
    subcol = "|     время(с)     |   перестановки   "
    print(f'|' + ' '*12 + subcol + ' ' + subcol*2 + '|')
    print('-'*129)
    le_dict = {
        0: 'Случайный ',
        1: 'Сорт.     ',
        2: 'Обратный  '
    }
    for i in range(3):
        line = f'| {le_dict[i]} | {times[0 + i]:^16.7g} |  {swaps[0 + i]:^16.7g} |'
        line += f' {times[3 + i]:^16.7g} | {swaps[3 + i]:^16.7g} |'
        line += f' {times[6 + i]:^16.7g} | {swaps[6 + i]:^16.7g} |'
        print(line)
        print('-'*129)


if __name__ == "__main__":
    main()
