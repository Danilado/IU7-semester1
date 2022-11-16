"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 10

Вычисление приближённого значения интеграла
===========================================

Вычисление приближённого значения интеграла
заданной в программе функции 
двумя способами
-------------------------------------------

1. Метод средних прямоугольников
2. Метод парабол

!!! В условиях лабораторной работы даны не самые чёткие
!!! указания по поиску n итерационным путём и т.д. и т.п.
!!! Я написал ряд проверок, которые можно поменять, комментируя
!!! и раскомментируя фрагменты кода
"""
# Самописная бибилиотека для ввода значений по всем правилам
import fast_inputs as fi
# Типизация
from typing import Callable

# для 1e-6 вычисления займут примерно 80 минут - протестировано
# для 1e-5 вычисления займут примерно 9 минут - протестировано
# для 1e-4 вычисления займут примерно 1 минуту - протестировано
eps = 1e-4


def antiderivative(x: float) -> float:
    """Первообразная заданной функции

    :param x: Аргумент
    :type x: float
    :return: Значние первообразной при данном значении аргумента
    :rtype: float
    """
    return x**3/3


def f(x: float) -> float:
    """Та самая заданная функция

    :param x: Аргумент
    :type x: float
    :return: Значние функции при данном значении аргумента
    :rtype: float
    """
    return x**2


def average_rectangles(start: float, finish: float,
                       segment_count: int, f: Callable) -> float:
    """Подсчёт интеграла методом средних прямоугольников или каких-то таких
    с равномерным разбиением на отрезки, то есть используя формулу
    средних прямоугольников на равномерной сетке
    source: https://ru.wikipedia.org/wiki/Метод_прямоугольников

    формула
    res = h * (f_0/2 + f_1 + ... + f_{n-1} + f_n/2)

    погрешность
    f"(eps)/24  *  h**3

    :param start: Начало отрезка интегрирования
    :type start: float
    :param finish: Конец отрезка интегрирования
    :type finish: float
    :param segment_count: Количество сегментов деления
    :type segment_count: int
    :param f: Интегрируемая функция
    :type f: Callable
    :return: Подсчитанное значение интеграла данной функции на данном отрезке
    :rtype: float
    """
    segment_count = int(segment_count)

    result = 0  # результат
    h = (finish - start)/segment_count  # длина отрезка

    for i in range(segment_count):
        result += f(start + h/2 + i*h)

    result *= h
    return result


def parabolas(start: float, finish: float,
              segment_count: int, f: Callable) -> float:
    """Подсчёт интеграла методом парабол
    source: http://www.cleverstudents.ru/integral/method_of_parabolas.html

    Формула
    h/3 * (f(x_0) + 4*sum(from i to n f(x_{2i-1})) + 2*sum(from i to n-1 f(x_{2i})) + f(x_{2n}))

    Погрешность
    (b-a) / 2880 * h**4 * |max(f""(x) on [start; finish])|

    :param start: Начало отрезка интегрирования
    :type start: float
    :param finish: Конец отрезка интегрирования
    :type finish: float
    :param segment_count: Количество сегментов деления
    :type segment_count: int
    :param f: Интегрируемая функция
    :type f: Callable
    :return: Подсчитанное значение интеграла данной функции на данном отрезке
    :rtype: float
    """
    segment_count = int(segment_count)

    h = (finish - start) / segment_count

    tmp_sum = 0

    x_0 = start
    x_1 = start + h

    for _ in range(segment_count - 1):
        tmp_sum += f(x_0) + 4*f(x_0 + h/2) + f(x_1)

        x_0 += h
        x_1 += h

    tmp_sum *= h/6

    return tmp_sum


def calculate_accurate_n(alg: Callable, start_n: int, finish_n: int,
                         fstart: int, ffinish: int) -> int:
    """Пытается посчитать более точное значение n за более-менее реальное время
    кастомизированным бинпоиском

    :param alg: Алгоритм, который нужно тестировать
    :type alg: Callable
    :param start_n: левый конец отрезка для бинпоиска
    :type start_n: int
    :param finish_n: правый конец отрезка для бинпоиска
    :type finish_n: int
    :param fstart: левый конец отрезка интегрирования
    :type fstart: int
    :param ffinish: правый конец отрезка интегрирования
    :type ffinish: int
    :return: посчитанное значение n
    :rtype: int
    """

    while finish_n - start_n > 1:
        mid = round((start_n + finish_n)/2)

        diff_mid = abs(
            alg(fstart, ffinish, mid, f) -
            alg(fstart, ffinish, 2*mid, f)
        )

        print(f"Разница для n = {mid} : {diff_mid:.7g}", end='\r')

        if diff_mid < eps:
            finish_n = mid
        else:
            start_n = mid

    return finish_n


def main():
    # Ввод отрезка интегрирования
    start_x = fi.param_input(
        float,
        custom_prompt="Введите значение x начала отрезка интегрирования: "
    )
    finish_x = fi.param_input(
        float,
        params=f'n>{start_x}',
        custom_prompt="Введите значение x конца отрезка интегрирования: "
    )
    # Ввод значний N1 и N2 - кол-ва участков разбиения
    N1 = fi.param_input(
        int,
        params='n>1',
        custom_prompt="Введите значение N1 - количество участков разбиения: "
    )
    N2 = fi.param_input(
        int,
        params='n>1',
        custom_prompt="Введите значение N2 - количество участков разбиения: "
    )

    # Интегрируем первым способом
    l1 = average_rectangles(start_x, finish_x, N1, f)
    l3 = average_rectangles(start_x, finish_x, N2, f)

    # Интегрируем вторым способом
    l2 = parabolas(start_x, finish_x, N1, f)
    l4 = parabolas(start_x, finish_x, N2, f)

    # Выводим таблицу
    # 13.7 - оптимальное значение для случаев с минусом и т.д.
    print()
    print(f"---------------------------------------------------------------")
    print(f"| Метод интегрирования          | N1: {N1:<8g} | N2: {N2:<8g} |")
    print(f"---------------------------------------------------------------")
    print(f"| Метод средних прямоугольников | {l1:<12.7g} | {l3:<12.7g} |")
    print(f"---------------------------------------------------------------")
    print(f"| Метод парабол                 | {l2:<12.7g} | {l4:<12.7g} |")
    print(f"---------------------------------------------------------------")
    print()

    integral = antiderivative(finish_x) - antiderivative(start_x)

    alg1_error = min(abs(l1 - integral), abs(l3 - integral))
    alg2_error = min(abs(l2 - integral), abs(l4 - integral))

    print(f"Посчитанный через первообразную интеграл: {integral:.7g}")

    if alg2_error < alg1_error:
        print("Метод парабол в данном случае более точен\n")
        least_error = alg2_error
        worst_alg = average_rectangles
    else:
        print("Метод средних прямоугольников в данном случае более точен\n")
        least_error = alg2_error
        worst_alg = parabolas

    n = 2
    diff_n = worst_alg(start_x, finish_x, 2, f)
    diff_2n = worst_alg(start_x, finish_x, 4, f)

    while True:
        # !!! Если нужно сравнивать не по формуле, а по настоящему интегралу
        # if abs(diff_n - integral) < eps:

        # !!! Если нужно сравнивать по формуле, но с минимальной погрешностью
        # if abs(diff_n - diff_2n) < least_error:

        # !!! Если нужно сравнивать не по формуле с минимальной погрешностью
        # if abs(diff_n - integral) < least_error:

        # !!! Если формула в итоге оказалась верна
        if abs(diff_n - diff_2n) < eps:
            print(' '*128, end='\r')
            break
        print(
            f"Вычисляю подходящее по параметрам n. Для n = {n} разница = {abs(diff_n-diff_2n):.7g}",
            end='\r'
        )

        n *= 2
        diff_n = diff_2n
        diff_2n = worst_alg(start_x, finish_x, 2*n, f)

    print(
        f'Вычисленное оптимальное значние n для худшей функции на данном отрезке: {n:.7g}\n'
    )

    """
    !!! В случае, если формула верна, то итерационно точное значние n
    !!! (минимально возможное) искать придётся дольше, чем проживёт вселенная
    !!! Поэтому я написал бинпоиск
    """

    low_error_flag = fi.param_input(
        str,
        r'[yYnN]|(Y|yes)|(N|no)|.{0}',
        "Попробовать посчитать более точное значение n? (N/y): "
    )

    low_error_flag = True if low_error_flag and low_error_flag[0] in 'Yy' else False

    if low_error_flag:
        # !!! Если сравнивать нужно с минимальной погрешностью из этих двух алгоритмов
        # eps = least_error

        # !!! Если нужно просить пользователя вводить эпсилон вручную
        # eps = fi.param_input(
        #     float,
        #     custom_prompt="Введите eps - точность, для которой нужно искать значние n: "
        # )

        accurate_n = calculate_accurate_n(
            worst_alg, n//2, n, start_x, finish_x)
        print(' '*128)
        print(f"Точное значние n: {accurate_n:.7g}")


if __name__ == '__main__':
    main()
