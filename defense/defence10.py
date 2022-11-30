"""Звягин Даниил ИУ7-13Б

методом серединных прямоуг
интеграл cos(x)
x [a; b]
eps вводится 
"""

from math import cos, sin


def mid_rects(a, b, eps):
    n = 2  # кол-во отрезков

    while True:
        h = (b - a)/n
        if abs(cos(a+h/2)*h) <= eps:
            break
        n *= 2

    x = a+h/2
    s = 0
    while x < b:
        s += cos(x)
        x += h

    s *= h
    return s


def main():
    a = float(input("Введите значение начала отрезка интегрирования: "))
    b = float(input("Введите значение конца отрезка интегрирования: "))
    eps = float(input("Введите желаемую точность вычислений: "))

    integral = mid_rects(a, b, eps)

    print(f"\nВычисленный интеграл: {integral:.7g}")
    print(f"Идеальный интеграл: {(sin(b)-sin(a)):.7g}")


if __name__ == "__main__":
    main()
