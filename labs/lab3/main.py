"""Звягин Даниил ИУ7-13Б

Лабораторная работа номер 3 - треугольник

Написать программу, которая по введенным целочисленным
координатам трех точек на плоскости вычисляет длины сторон
образованного треугольника и длину медианы, проведенной из
наибольшего угла.

Определить, является ли треугольник остроугольным.

Далее вводятся координаты точки. Определить, находится ли
точка внутри треугольника. Если да, то найти расстояние от точки
до ближайшей стороны треугольника.
"""

import math as m


eps = 1e-8
xA = yA = xB = yB = xC = yC = None

# Ввод
while type(xA) != int:
    xA = input("Введите координатy x точки A: ")

    # Проверяем ввод на ошибки
    try:
        xA = int(xA)
    except ValueError:
        print(
            "Введены данные неверного типа " +
            f"({type(xA)}, ожидался int)"
        )
        continue

while type(yA) != int:
    yA = input("Введите координатy y точки A: ")

    # Проверяем ввод на ошибки
    try:
        yA = int(yA)
    except ValueError:
        print(
            "Введены данные неверного типа " +
            f"({type(yA)}, ожидался int)"
        )
        continue

print()  # Пустая строка - разделитель
while True:
    while type(xB) != int:
        xB = input("Введите координатy x точки B: ")

        # Проверяем ввод на ошибки
        try:
            xB = int(xB)
        except ValueError:
            print(
                "Введены данные неверного типа " +
                f"({type(xB)}, ожидался int)"
            )
            continue

    while type(yB) != int:
        yB = input("Введите координатy y точки B: ")

        # Проверяем ввод на ошибки
        try:
            yB = int(yB)
        except ValueError:
            print(
                "Введены данные неверного типа " +
                f"({type(yB)}, ожидался int)"
            )
            continue

    if xA == xB and yA == yB:
        print("Точка B не может совпадать с точкой A")
        xB = yB = None
    else:
        break

print()  # Пустая строка - разделитель
while True:
    while type(xC) != int:
        xC = input("Введите координатy x точки C: ")

        # Проверяем ввод на ошибки
        try:
            xC = int(xC)
        except ValueError:
            print(
                "Введены данные неверного типа " +
                f"({type(xC)}, ожидался int)"
            )
            continue

    while type(yC) != int:
        yC = input("Введите координатy y точки C: ")

        # Проверяем ввод на ошибки
        try:
            yC = int(yC)
        except ValueError:
            print(
                "Введены данные неверного типа " +
                f"({type(yC)}, ожидался int)"
            )
            continue

    if yA == yB == yC or xA == xB == xC:
        print("Точка C не может лежать на одной прямой с точками А и В")
        xC = yC = None
    elif xA != xB and yA != yB:
        if (xC - xA)/(xB - xA) == (yC - yA)/(yB - yA):
            print("Точка C не может лежать на одной прямой с точками А и В")
            xC = yC = None
    elif xC == xA and yC == yA:
        print("Точка C не может совпадать с точкой A")
        xC = yC = None
    elif xC == xB and yC == yB:
        print("Точка C не может совпадать с точкой B")
        xC = yC = None
    else:
        break

"""
Приступаем к непосредственному выполнению задачи

Чтобы найти длину отрезка, имея координаты точек
его концов, нужной найти длину вектора, 
построенного на этих точках, то есть, проще говоря,
воспользоваться теоремой пифагора

|AB| = sqrt((x2-x1)**2 + (y2-y1)**2))
"""

print('\n')  # Визуально отделяю ввод от вывода

# Найдём длину стороны AB
AB = m.sqrt((xB - xA)**2 + (yB - yA)**2)
print(f"Длина стороны AB: {AB:.7g}")

# Найдём длину стороны BC
BC = m.sqrt((xC - xB)**2 + (yC - yB)**2)
print(f"Длина стороны BC: {BC:.7g}")

# Найдём длину стороны AC
AC = m.sqrt((xC - xA)**2 + (yC - yA)**2)
print(f"Длина стороны AC: {AC:.7g}\n")

# Буду опираться на то, что наибольший
# угол лежит напротив наибольшей стороны

# Координаты точки начала медианы
spointx = spointy = None

# Координаты конца медианы
fpointx = fpointy = None

# Длина наибольшей стороны - на будущее
maxside = 0

if AB > BC:
    if AB > AC:
        # AB - наибольшая сторона
        maxside = AB

        spointx = xC
        spointy = yC

        # Середина стороны
        fpointx = xA + (xB - xA) / 2
        fpointy = yA + (yB - yA) / 2

    else:
        # AC - наибольшая сторона
        maxside = AC

        spointx = xB
        spointy = yB

        # Середина стороны
        fpointx = xA + (xC - xA) / 2
        fpointy = yA + (yC - yA) / 2

elif BC > AC:
    # BC - наибольшая сторона
    maxside = BC

    spointx = xA
    spointy = yA

    # Середина стороны
    fpointx = xB + (xC - xB) / 2
    fpointy = yB + (yC - yB) / 2

else:
    # AC - наибольшая сторона
    maxside = AC

    spointx = xB
    spointy = yB

    # Середина стороны
    fpointx = xA + (xC - xA) / 2
    fpointy = yA + (yC - yA) / 2

med = m.sqrt((fpointx - spointx)**2 + (fpointy - spointy)**2)
print(
    "Длина медианы, проведённой из наибольшего " +
    f"угла: {med:.7g}\n"
)

"""
Определим, является ли треугольник остроугольным

(квадрат наибольшей стороны должен быть меньше 
суммы квадратов других сторон)
"""

tmp_delta = maxside**2 - (AB**2 + BC**2 + AC**2 - maxside**2)
if abs(tmp_delta) < eps:
    print("Треугольник не остроугольный\n")
elif tmp_delta < 0:
    print("Треугольник остроугольный\n")
else:
    print("Треугольник не остроугольный\n")

xP = yP = None

while type(xP) != float:
    xP = input("Введите координатy x точки P: ")

    # Проверяем ввод на ошибки
    try:
        xP = float(xP)
    except ValueError:
        print(
            "Введены данные неверного типа " +
            f"({type(xP)}, ожидался float)"
        )
        continue

while type(yP) != float:
    yP = input("Введите координатy y точки P: ")

    # Проверяем ввод на ошибки
    try:
        yP = float(yP)
    except ValueError:
        print(
            "Введены данные неверного типа " +
            f"({type(yP)}, ожидался float)"
        )
        continue

"""
Чтобы определить, находится ли точка внутри треугольника,
найдём длины отрезков от вершин треугольника до данной точки

Затем найдем площади трёх образованных треугольников и
если они в сумме дают площадь основного треугольника,
значит точка лежит внутри него 
"""

AP = m.sqrt(abs(xP - xA) ** 2 + abs(yP - yA) ** 2)
BP = m.sqrt(abs(xP - xB) ** 2 + abs(yP - yB) ** 2)
CP = m.sqrt(abs(xP - xC) ** 2 + abs(yP - yC) ** 2)

# Полупериметр для формулы Герона
p = (AB + BC + AC) / 2

main_area = m.sqrt(p * (p - AB) * (p - BC) * (p - AC))

p = (AB + BP + AP) / 2
area_1 = m.sqrt(p * (p - AB) * (p - BP) * (p - AP))

p = (BP + BC + CP) / 2
area_2 = m.sqrt(p * (p - BP) * (p - BC) * (p - CP))

p = (AP + CP + AC) / 2
area_3 = m.sqrt(p * (p - AP) * (p - CP) * (p - AC))

if abs(main_area - area_1 - area_2 - area_3) < eps:
    print("\nТочка лежит внутри треугольника\n")

    dist_1 = area_1 / AB * 2
    dist_2 = area_2 / BC * 2
    dist_3 = area_3 / AC * 2

    print(
        f"Расстояние до ближайшей стороны: {min(dist_1, dist_2, dist_3):.7g}"
    )

else:
    print("\nТочка лежит вне треугольника\n")
