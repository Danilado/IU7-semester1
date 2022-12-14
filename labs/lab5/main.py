"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 5

Сумма бесконечного ряда

Вариант 68
(-1)**(n-1) * x**n * (1 * 3 *...* (2n-3)) / (2 * 4 *...* 2n)
"""

from math import isnan, isinf


# Ввод
x = float(input("Введите значение аргумента (float): "))
eps = float(input("Введите желаемую точность вычислений (float): "))

iteration_limit = int(input(
    "Введите максимальное количество итераций (int, >=0): "
))

if iteration_limit < 0:
    print("Введено неправильное значение ограничения!")
    exit()

log_step = int(input(
    "Введите значение шага вывода (int,  >0): "
))
if log_step < 0:
    print("Введено неправильное значение шага, оно будет заменено на 1")
    log_step = 1
if iteration_limit != 0 and log_step > iteration_limit:
    print("Шаг вывода больше, чем лимит итераций, но кто я такой, чтобы вас судить...")

# Голова таблицы
print('\n')
print("------------------------------------------------")
print("| Итерация   |   t            |   s            |")
print("------------------------------------------------")

# Флажки для корректной работы вывода
error_flag = 0
success_flag = 0
last_n = 0

# Сумма ряда и значеие дроби (для того, чтобы избегать переполнения)
inf_sum = 0
ratio = 1.0
for n in range(iteration_limit):

    # Считаем страшную дробь
    if n > 2:
        ratio *= (2*n - 3)
    if n > 0:
        ratio /= 2*n

    x_n = x
    for i in range(n):
        x_n *= x

    if isinf(x):
        error_flag = 1
        break

    # Считаем текущий элемент
    cur_el = (-1)**(n+1) * x_n * ratio

    # Проверяем на ошибки деления и умножения флоатов
    if isnan(cur_el) or isinf(cur_el):
        error_flag = 1
        break

    # Прибавляем
    inf_sum += cur_el

    # Выводим с требуемым шагом
    if n % log_step == 0:
        print(f"| {n+1:^10.6g} | {cur_el:^14.6g} | {inf_sum:^14.6g} |")

    # Проверка точности
    if abs(cur_el) < eps:
        success_flag = 1
        last_n = n + 1
        break

print("------------------------------------------------\n")

# Вывод
if error_flag:
    print(
        "Дальнейшие вычисления вызывают переполнение!"
    )

if not success_flag:
    """ ⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
    ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
    ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
    ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷"""
    print("Не удалось достичь желаемой точности за указанное число итераций")
    # print(f"Вот, сумма, которую удалось посчитать: {inf_sum:7g}")

else:
    print(
        f"Сумма бесконечного ряда: {inf_sum:7g}, " +
        f"вычислена за {last_n} итераций"
    )
