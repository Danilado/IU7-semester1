"""Генератор новой ДБшки"""
from typing import List, Union
from random import random, randint


def generate() -> List[List[Union[int, str, int, int, int, int, bool, float]]]:
    names = "Дима Кирилл Виталя Богдан Максим Серёжа Наташа Рома Егор Даня".split()

#       ID      NAME    S_YEAR  F_YEAR  AGE     AMOUNT  SA      LGW
#       int     str     int     int     int     int     bool    float

    db = []
    for i in range(10):
        tmp_i = randint(0, len(names)-1)
        name = names.pop(tmp_i)

        start_year = randint(2005, 2018)
        end_year = randint(start_year, 2022)

        age = 2022 - start_year

        sa = bool(randint(0, 1))

        amount = end_year - start_year
        if sa:
            amount += randint(0, age - amount)

        lgw = round(random()*10, 2)

        db.append([i+1, name, start_year, end_year, age, amount, sa, lgw])

    return db
