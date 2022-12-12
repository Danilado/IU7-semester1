"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 14
База данных в бинарном файле

Структуру базы данных можно посмотреть 
в прерыдущей лабораторной работе

Функционал
1. Выбрать файл для работы
2. Инициализировать БД
3. Вывести содержимое БД
4. Добавить запись в произвольное место
5. Удалить любую запись из БД
6. Поиск по одному полю
7. Поиск по двум полям
"""

import struct
import fast_inputs as fi
import generate_db
from itertools import count
from typing import List, Union
import os
import re
current_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_path)

# Формат одной строки в базе данных
# Строка из 12 символов, 4 беззнаковых числа,
# булевое значение, число двойой точности
DB_FORMAT = "12s 4L ? d"

# Размер одной строки ДБ в байтах
# (для правильного чтения)
CHUNK_SIZE = struct.calcsize(DB_FORMAT)


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
    if len(line) != 7:
        return False

    line = list(line)

    line[1] = int(line[1])
    line[2] = int(line[2])
    line[3] = int(line[3])
    line[4] = int(line[4])
    line[6] = float(line[6])

    if line[1] > 2022 or line[2] > 2022:
        return False

    elif line[1] > line[2]:
        return False

    elif line[3] != 2022 - line[1]:
        return False

    elif line[4] < line[2] - line[1]:
        return False

    return True


def open_file(filename: str) -> str:
    """Проверяет, файл по заданному пути
    на соответствие формату базы данных

    :param filename: Имя файла с путём к нему
    :type filename: str
    :return: имя файла, если всё хорошо, иначе - None
    :rtype: str
    """
    with open(filename, 'rb') as f:
        fin = os.SEEK_END

        while os.SEEK_CUR < fin:
            try:
                line = f.read(CHUNK_SIZE)

                if not line:
                    break

                db_line = struct.unpack(DB_FORMAT, line)

                if not validate_line(db_line):
                    raise struct.error

            except struct.error:
                print("Файл повреждён или не является соответствующей БД")
                return None

    return filename


def input_line() -> List[Union[int, str, int, int, int, int, bool, float]]:
    """Осущетсвляет ввод строки базы данных

    :return: строка
    :rtype: List[Union[int, str, int, int, int, int, bool, float]]
    """

    line = []
    line.append(bytes(fi.param_input(
        str, r'^\S{2,12}$', "Введите имя: "), "utf-8"))
    line.append(fi.param_input(int, f'2005<=n<2023',
                "Введите год рождения ребёнка: "))
    line.append(fi.param_input(
        int, f'{line[1]}<=n<2023', "Введите окончания верования: "))
    line.append(2022 - line[1])
    line.append(fi.param_input(
        int, f'n>={line[2] - line[1]}', "Введите кол-во полученных ребёнком подарков: "))
    still_asks_flag = fi.param_input(
        str,
        r'([Yy]([Ee][Ss])?)|([Nn][Oo]?)|.{0}',
        "Просит ли ребёнок подарки до сих пор? [N/y]: "
    )
    if not still_asks_flag or re.fullmatch(still_asks_flag, r'[Nn][Oo]?'):
        line.append(False)
    else:
        line.append(True)
    line.append(fi.param_input(
        float, 'n>0', "Введите вес последнего подарка, подаренного ребёнку: "))

    if validate_line(line):
        return line
    else:
        print("В строке каким-то образом нашлась ошибка, попробуйте снова")
        return input_line()


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

    # Триггерит PermissionError
    with open(filename, 'w', encoding='utf-8') as f:
        ...

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
        # Файл очищен в 161 строке
        with open(filename, 'ab') as f:
            for line in generate_db.generate():
                f.write(struct.pack(
                    DB_FORMAT,
                    *line))
        print(f"\nЗаполнен файл {filename}\n")

    else:

        print("Когда вам надоест вводить строки, нажмите ctrl+c")

        db = []
        for i in count(1):

            print(f"\nВвод {i}-й строки, для выхода нажмите ctrl+c")

            try:
                db.append(input_line())
            except KeyboardInterrupt:
                break

        # Файл очищен в 161 строке
        with open(filename, 'ab') as f:
            for line in db:
                f.write(struct.pack(DB_FORMAT, *line))
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
        with open(filename, 'rb') as f:
            try:
                _ = struct.unpack(DB_FORMAT, f.read(CHUNK_SIZE))
            except struct.error or OSError:
                print("Файл пустой или повреждён и не соответствует формату БД")
                return 1
            f.seek(0)

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
AGE     -   Возраст
AMOUNT  -   Кол-во подарков
SA      -   Просит до сих пор
LGW     -   Вес последнего подарка
""")
                print()

            print("ID\tNAME\t\tS_YEAR\tF_YEAR\tAGE\tAMOUNT\tSA\tLGW")

            counter = 1
            while True:
                try:
                    chunk = f.read(CHUNK_SIZE)
                    if not chunk:
                        break

                    line = struct.unpack(DB_FORMAT, chunk)
                    line = list(line)
                    line[0] = line[0].decode()
                    print(counter, end='\t')
                    print(line[0], end='\t\t')
                    print(*line[1:], sep='\t')
                    counter += 1

                except OSError:
                    break
                except struct.error:
                    print("Далее файл повреждён")
                    return 1

    except FileNotFoundError:
        print("С файлом что-то случилось")
        return 1


def add_line(filename: str, index: int) -> None:
    """Записывает строку в конец файла

    :param filename: Имя файла (с путём)
    :type filename: str
    :param index: Индекс строки для вставки
    :type index: int
    """
    if not filename:
        print("Сначала откройте файл!")
        return 1

    try:
        new_line = input_line()
        # Раз уж нам нельзя всё сохранить, будем перемещать
        line_count = os.path.getsize(filename)//CHUNK_SIZE
        with open(filename, 'r+b') as f:
            f.seek(-CHUNK_SIZE, os.SEEK_END)

            while line_count > index-1:
                prev_chunk = f.read(CHUNK_SIZE)
                f.write(prev_chunk)
                if index == 1:
                    if line_count - index != 0:
                        f.seek(-CHUNK_SIZE*3, os.SEEK_CUR)
                    else:
                        f.seek(0)
                else:
                    f.seek(-CHUNK_SIZE*3, os.SEEK_CUR)
                line_count -= 1

            if index != 1:
                f.seek(CHUNK_SIZE, os.SEEK_CUR)
            f.write(struct.pack(DB_FORMAT, *new_line))

        return 0

    except FileNotFoundError:
        print("С файлом что-то случилось")
        return 1


def remove_line(filename: str, index: int) -> None:
    """Удаляет произвольную строку из БД

    :param filename: имя файла
    :type filename: str
    :param index: Индекс удаляемой строки
    :type index: int
    """
    if not filename:
        print("Сначала введите имя файла!")
        return 1

    try:
        with open(filename, "r+b") as f:
            f.seek(CHUNK_SIZE*index)
            while True:
                line = f.read(CHUNK_SIZE)
                if not line:
                    break
                f.seek(-CHUNK_SIZE*2, os.SEEK_CUR)
                f.write(line)
                f.seek(CHUNK_SIZE, os.SEEK_CUR)

            f.truncate(os.path.getsize(filename)-CHUNK_SIZE)

        print(f"Строка {index} успешно стёрта")
    except FileNotFoundError:
        print("С фалом что-то случилось")
        return 1


def find_by_name(filename: str, query: str) -> None:
    """Ищет и выводит строки базы данных, значение
    ячейки имени в которых соответствует введённому

    :param filename: Имя файла (с путём)
    :type filename: str
    :param query: Срока поиска
    :type query: str
    """
    try:
        with open(filename, 'rb') as f:
            line = f.read(CHUNK_SIZE)
            if not line:
                print("Файл пустой!")
                return 1

            found_something = False

            while line:
                cells = list(struct.unpack(DB_FORMAT, line))

                if cells[0].decode() == query:
                    cells[0] = cells[0].decode()
                    print(*cells, sep='\t')

                    found_something = True
                line = f.read(CHUNK_SIZE)

        if not found_something:
            print("По вашему запросу ничего не нашлось")
    except FileNotFoundError:
        print("С файлом что-то случилось")
        return 1


def find_by_two_fields(filename: str, query1: int, query2: int) -> None:
    """Ищет и выводит строки базы данных, значения
    ячеек возраста и кол-ва полученных подарков
    в которых соответствует введённым значениям

    :param filename: Имя файла (с путём)
    :type filename: str
    :param query1: Срока поиска 1
    :type query1: str
    :param query2: Срока поиска 2
    :type query2: str
    """
    try:
        with open(filename, 'rb') as f:
            line = f.read(CHUNK_SIZE)
            if not line:
                print("Файл пустой!")
                return 1

            found_something = False

            while line:
                cells = list(struct.unpack(DB_FORMAT, line))
                if cells[3] == query1 and cells[4] == query2:
                    cells[0] = cells[0].decode()
                    print(*cells, sep='\t')
                    found_something = True
                line = f.read(CHUNK_SIZE)

        if not found_something:
            print("По вашему запросу ничего не нашлось")
    except FileNotFoundError:
        print("С файлом что-то случилось")
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
        print("4: Добавить запись в базу данных         ")
        print("5: Удалить строку из БД                  ")
        print("6: Поиск по одному полю                  ")
        print("7: Поиск по двум полям                   ")
        print("0: Выход                                 ")

        command = fi.param_input(int, "0<=n<=7", '\nВведите номер команды: ')
        clear()
        print(f"> {command}")

        try:
            if command == 0:
                running = False
                print("До свидания")
            elif command == 1:
                file_path = fi.input_filename(1, current_dir)
                filename = open_file(file_path)
            elif command == 2:
                file_path = fi.input_filename(2, current_dir)
                filename = db_init(file_path)
            elif filename:
                if command == 3:
                    print_db(filename)
                elif command == 4:
                    max_id = os.path.getsize(filename)//CHUNK_SIZE+1
                    index = fi.param_input(
                        int,
                        f"1<=n<={max_id}",
                        "Введите номер записи для вставки: "
                    )
                    add_line(filename, index)
                elif command == 5:
                    max_id = os.path.getsize(filename)//CHUNK_SIZE
                    index = fi.param_input(
                        int,
                        f"1<=n<={max_id}",
                        "Введите номер записи для удаления: "
                    )
                    remove_line(filename, index)
                elif command == 6:
                    query = fi.param_input(
                        str,
                        '\S{2,12}',
                        "Введите имя ребёнка для поиска в базе данных: "
                    )
                    find_by_name(filename, query)
                else:
                    query1 = fi.param_input(
                        int,
                        '0<n<18',
                        'Введите возраст ребёнка для поиска: '
                    )
                    query2 = fi.param_input(
                        int,
                        'n>0',
                        "Введите кол-во подарков, полученных ребёнком: "
                    )
                    find_by_two_fields(filename, query1, query2)
            else:
                print("Сначала откройте файл!")
        except PermissionError:
            print("Недостаточно прав для доступа к данному файлу или каталогу")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nВсего доброго")
