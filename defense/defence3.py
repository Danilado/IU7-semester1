"""Звягин Даниил ИУ7-13Б

Защита лабораторной работы номер 4
Найти длину биссектрисы, проведённой 
из наименьшего угла
"""

import math as m

xA = int(input("Введите значение x точки А: "))
yA = int(input("Введите значение y точки А: "))

xB = int(input("Введите значение x точки B: "))
yB = int(input("Введите значение y точки B: "))

xC = int(input("Введите значение x точки C: "))
yC = int(input("Введите значение y точки C: "))

AB = m.sqrt( (xB - xA) ** 2 + (yB - yA) ** 2 )
BC = m.sqrt( (xC - xB) ** 2 + (yC - yB) ** 2 )
AC = m.sqrt( (xC - xA) ** 2 + (yC - yA) ** 2 )

if AB < BC:
    if AB < AC:
        #  AB - наименьший
        #  Из угла C
        
        ratio = BC / (AC + BC)

        deltaX = ratio * (xA - xB)
        deltaY = ratio * (yA - yB)

        xP = xB + deltaX
        yP = yB + deltaY



        length = m.sqrt( (xP - xC)**2 + (yP - yC)**2 )

    else:
        #  AC - наименьший
        #  Из угла B
        
        ratio = BC / (AB + BC)

        deltaX = ratio * (xC - xA)
        deltaY = ratio * (yC - yA)

        xP = xC + deltaX
        yP = yC + deltaY

        length = m.sqrt( (xP - xB)**2 + (yP - yB)**2 )

else:
    if BC < AC:
        #  BC - наименьший
        #  Из угла A
        
        ratio = AB / (AB + AC)

        deltaX = ratio * (xC - xB)
        deltaY = ratio * (yC - yB)

        xP = xB + deltaX
        yP = yB + deltaY

        length = m.sqrt( (xP - xA)**2 + (yP - yA)**2 )

    else:
        #  AC - наименьший
        #  Из угла B
        
        ratio = BC / (AB + BC)

        deltaX = ratio * (xC - xA)
        deltaY = ratio * (yC - yA)

        xP = xA + deltaX
        yP = yA + deltaY

        length = m.sqrt( (xP - xB)**2 + (yP - yB)**2 )

print(f"\nxP: {xP} yP: {yP}")
print(
    "\nДлина биссекриссы, проведённый из наименьшего угла"+
    f" равна: {length:.7g}"
    )