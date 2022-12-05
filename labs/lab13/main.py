"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 13
Работа с файлами - базы данных

Функционал

Создать ДБ:
    Ввод имени файла
    Сохранение в текстовом файле базы 
      данных в любом удобном мне виде

Считать ДБ:
    Ввод имени файла
    Вывод на экран содержимого базы 
      данных

Записать строку в ДБ:
    Ввод имени файла
    Ввод очередной строки
    Запись строки в конец файла с 
      сохранением

Найти по полю в ДБ:
    Ввод имени файла
    Поиск записи в базе по выбранному мной
      столбцу

Найти по двум полям в ДБ:
    Ввод имени файла
    Поиск записи в базе данных по двум полям
"""

"""СТРУКТУРА
База данных детей и их верования в Деда Мороза

ID      - Номер
NAME    - Имя ребёнка
S_YEAR  - Год начала верования
F_YEAR  - Год конца верования
AGE     - Возраст ребёнка
AMOUNT  - Кол-во полученных подарков
SA      - Still_Asks Просит ли до сих под подарки у деда мороза
LGW     - Last_Gift_Weight вес последнего подарка

ID      NAME    S_YEAR  F_YEAR  AGE     AMOUNT  SA      LGW         
int     str     int     int     int     int     bool    float
"""


from itertools import count
from typing import List, Union
import generate_db
import fast_inputs as fi
import os
import re
current_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_path)


def clear():
    """Очищает экран"""
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_line(line: List[str]) -> bool:
    """Проверяет на валидность строчку ДБшки

    :param line: Строка ДБшки
    :type line: List[str]
    :return: True, если всё хорошо иначе False
    :rtype: bool
    """
    error_flag = False

    if len(line) != 8:
        print("Кол-во ячеек в строке не сооветствует стандарту ДБ")
        print(*line, '\n')
        return False

    try:
        if line[6] != "True" and line[6] != "False":
            print('6-й пункт')
            raise TypeError

        line[0] = int(line[0])
        line[2] = int(line[2])
        line[3] = int(line[3])
        line[4] = int(line[4])
        line[5] = int(line[5])
        line[6] = False if line[6] == "False" else True
        line[7] = float(line[7])
    except TypeError:
        print("Ошибка: формата данных в строке")
        print(*line, '\n')
        return False

    if line[0] < 1:
        print("Ошибка: ID меньше 1")
        error_flag = True

    if not 2 < len(line[1]) < 12:
        print("Ошибка: Длина имени не в промежутке [2; 12]")
        error_flag = True

    if line[2] > 2022 or line[3] > 2022:
        print("Ошибка: Значения полей, обозначающих годы больше текущего года")
        error_flag = True

    if line[2] > line[3]:
        print("Ошибка: Год начала верования больше года окончания верования")
        error_flag = True

    if line[4] != 2022 - line[2]:
        print("Ошибка: Возраст не соответствует посчитанному значению")
        error_flag = True

    if line[5] < line[3] - line[2]:
        print("Ошибка: Кол-во полученных подарков меньше посчитанного минимума")
        error_flag = True

    if error_flag:
        print(*line, '\n')
        return False
    return True


def input_line(i: int) -> List[Union[int, str, int, int, int, int, bool, float]]:
    """Осущетсвляет ввод строки базы данных

    :return: строка
    :rtype: List[Union[int, str, int, int, int, int, bool, float]]
    """

    line = []
    line.append(i)
    line.append(fi.param_input(str, r'^\S{2,12}$', "Введите имя: "))
    line.append(fi.param_input(int, f'2005<=n<2023',
                "Введите год рождения ребёнка: "))
    line.append(fi.param_input(
        int, f'{line[2]}<=n<2023', "Введите окончания верования: "))
    line.append(2022 - line[2])
    line.append(fi.param_input(
        int, f'n>={line[3] - line[2]}', "Введите кол-во полученных ребёнком подарков: "))
    still_asks_flag = fi.param_input(
        str,
        r'([Yy]([Ee][Ss])?)|([Nn][Oo]?)|.{0}',
        "Просит ли ребёнок подарки до сих пор? [N/y]: "
    )
    if not still_asks_flag or re.fullmatch(still_asks_flag, r'[Nn][Oo]?'):
        line.append("False")
    else:
        line.append("True")
    line.append(fi.param_input(
        float, 'n>0', "Введите вес последнего подарка, подаренного ребёнку: "))

    if validate_line(line):
        return line
    else:
        return input_line(i)


def unparse(db: List[List[Union[int, str, int, int, int, int, bool, float]]]) -> str:
    """Превращает базу данных в список строк (формата str)

    :param db: База данных
    :type db: List[List[Union[int, str, int, int, int, int, bool, float]]]
    :return: Список строк
    :rtype: List[str]
    """
    unparsed = []
    for line in db:
        str_line = ''
        for i, el in enumerate(line):
            if i == len(line)-1:
                str_line += str(el) + '\n'
            else:
                str_line += str(el) + '|'

        unparsed.append(str_line)
    unparsed[-1] = unparsed[-1].strip()
    return unparsed


def open_file(filename: str) -> str:
    """Проверяет, файл по заданному пути
    на соответствие формату базы данных

    :param filename: Имя файла с путём к нему
    :type filename: str
    :return: имя файла, если всё хорошо, иначе - None
    :rtype: str
    """

    with open(filename, 'r', encoding="utf-8") as f:
        for i in count(1):
            line = f.readline()

            if not line:
                if i == 1:
                    print("WARNING: Файл пустой\n")
                break

            db_line = line.split('|')

            if not validate_line(db_line):
                return None

    print()
    return filename


def db_init(filename: str) -> str:
    """Осуществляет создание базы данных
    по заданному пути

    :param filename: имя (и путь) файля для создания базы данных
    :type filename: str
    :return: Имя файла, если создание прошло успешно
    :rtype: str
    """
    if os.path.isfile(filename):
        continue_flag = fi.param_input(
            str,
            r'([Yy]([Ee][Ss])?)|([Nn][Oo]?)|.{0}',
            "WARNING: Файл с таким именем уже существует. \nЭто действие сотрёт содержимое файла. Продолжить? [N/y]: "
        )

        if not continue_flag or continue_flag in "NONononO":
            return None

    fill_flag = fi.param_input(
        str,
        r'([Yy]([Ee][Ss])?)|([Nn][Oo]?)|.{0}',
        "Хотите заполнить базу данных (будет предоставлен выбор: вручную или случайно)? [N/y]: "
    )

    if not fill_flag or fill_flag in "NONononO":
        open(filename, 'w', encoding='utf-8').close()
        return filename

    random_fill_flag = fi.param_input(
        str,
        r'([Yy]([Ee][Ss])?)|([Nn][Oo]?)|.{0}',
        "Хотите заполнить базу данных случайными значениями? [Y/n]: "
    )

    if not random_fill_flag or re.fullmatch(random_fill_flag, r'[Yy]([Ee][Ss])?'):
        with open(filename, 'w', encoding='utf-8') as f:
            for line in unparse(generate_db.generate()):
                f.write(line)
        print(f"\nЗаполнен файл {filename}\n")
    else:
        print("Когда вам надоест вводить строки, нажмите ctrl+c")
        db = []
        for i in count(1):
            print(f"\nВвод {i}-й строки, для выхода нажмите ctrl+c")
            try:
                db.append(input_line(i))
            except KeyboardInterrupt:
                break

        with open(filename, 'w', encoding='utf-8') as f:
            for line in unparse(db):
                f.write(line)
        print(f"\nЗаполнен файл {filename}\n")

    return filename


def print_db(filename: str) -> None:
    """Ввыводит содержимое базы данных на экран

    :param filename: Имя файла (с путём)
    :type filename: str
    """
    if not filename:
        print("Сначала откройте файл!")
        return 1

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            line = f.readline()
            if not line:
                print("Файл пустой!")
                return 0
            f.seek(0)
            # ID      NAME    S_YEAR  F_YEAR  AGE     AMOUNT  SA      LGW

            help_flag = fi.param_input(
                str,
                r'([Yy]([Ee][Ss])?)|([Nn][Oo]?)|.{0}',
                "Вывести памятку по значениям полей базы данных? [N/y]: "
            )

            if help_flag and help_flag not in "NoNOnonO":
                print("""
ID      -   ID
NAME    -   Имя ребёнка
S_YEAR  -   Год рождения
F_YEAR  -   Год конца верования
"AGE    -   Возраст
AMOUNT  -   Кол-во подарков
SA      -   Просит до сих пор
LGW     -   Вес последнего подарка
""")
                print()

            print("ID\tNAME\t\tS_YEAR\tF_YEAR\tAGE\tAMOUNT\tSA\tLGW")

            while line:
                line = f.readline().strip()
                if not line:
                    break
                args = line.split('|')
                print(args[0], end='\t')
                print(args[1], end='\t'*(2-len(args[1])//8))
                print(*args[2:], sep='\t')
    except FileNotFoundError:
        print("С файлом что-то случилось")
        return 1


def add_line(filename: str) -> None:
    """Записывает строку в конец файла

    :param filename: Имя файла (с путём)
    :type filename: str
    """
    if not filename:
        print("Сначала откройте файл!")
        return 1

    try:
        with open(filename, 'rb') as f:
            try:
                f.seek(-4, os.SEEK_END)
                while f.read(1) != b'\n':
                    # Идём seek-ом в начало последней не пустой строки
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                f.seek(0)  # Если одна строка

            # С ДНЁМ МИЛЛИОНА МЕТОДОВ
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
            # ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
            # ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
            # ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
            # ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
            last_index = int(f.readline().decode().strip().split('|')[0])

        new_line = input_line(last_index+1)

        with open(filename, 'a', encoding='utf-8') as f:
            text_line = ''
            for i, el in enumerate(new_line):
                text_line += str(el)
                if i != 7:
                    text_line += '|'
            f.write(text_line)

        return 0

    except FileNotFoundError:
        print("С файлом что-то случилось")
        return 1
    except TypeError:
        print("С последней строкой файла что-то не так")
        return 1


def main():
    print("Вас приветствует процессор баз дынных INJIR_DBS")
    running = True
    filename = None
    command = None

    while running:
        print()
        if not filename:
            print("Сейчас работаю с файлом N/A")
        else:
            print(f"Сейчас работаем с файлом {filename}")

        print()
        print("Меню:                                    ")
        print("1: Выбрать файл для работы               ")
        print("2: Инициализировать базу данных          ")
        print("3: Вывести содержимое базы данных        ")
        print("4: Добавить запись в конец базы данных   ")
        print("5: Поиск по одному полю                  ")
        print("6: Поиск по двум полям                   ")
        print("0: Выход                                 ")

        command = fi.param_input(int, "0<=n<=6", '\nВведите номер команды: ')
        clear()
        print(f"> {command}")

        if command == 0:
            running = False
        elif command == 1:
            file_path = fi.input_filename(1, current_dir)
            filename = open_file(file_path)
        elif command == 2:
            file_path = fi.input_filename(2, current_dir)
            filename = db_init(file_path)
        elif command == 3:
            print_db(filename)
        elif command == 4:
            add_line(filename)
        else:
            ...


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nВсего доброго")
