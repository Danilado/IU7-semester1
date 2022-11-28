"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 12

Тексторый процессор
============================
"""
import os
import re
import fast_inputs as fi
from typing import List, Callable, Union


"""Дуглас Адамс - Автостопом по галактике

— Сорок два! — взвизгнул Лунккуоол. — И это всё, что ты можешь сказать после семи с половиной миллионов лет работы?

— Я всё очень тщательно проверил, — сказал компьютер, — и со всей определённостью заявляю, что это и есть ответ. 
  Мне кажется, если уж быть с вами абсолютно честным, то всё дело в том, что вы сами не знали, в чём вопрос.

— Но это же великий вопрос! Окончательный вопрос жизни, Вселенной и всего такого! — почти завыл Лунккуоол.

— Да, — сказал компьютер голосом страдальца, просвещающего круглого дурака. — И что же это за вопрос?
"""


def clear():
    """Очищает экран"""
    os.system('cls' if os.name == 'nt' else 'clear')


def output_text(text: List[str]):
    """Выводит текст

    :param text: Текст для вывода
    :type text: List[str]
    """
    for line in text:
        print(line)
    print()


def align_left(text: List[str]) -> List[str]:
    """Выравнивает текст по левой стороне экрана

    :param text: Текст для форматирования
    :type text: List[str]
    :return: Отформатированный текст
    :rtype: List[str]
    """

    for i in range(len(text)):
        text[i] = text[i].strip()
        while "  " in text[i]:
            text[i] = text[i].replace("  ", " ")

    clear()
    print("> 1\n")
    return text


def align_right(text: List[str]) -> List[str]:
    """Выравнивает текст по правой стороне
    (по длине самой большой строки)

    :param text: Текст для форматирования
    :type text: List[str]
    :return: Отформатированный текст
    :rtype: List[str]
    """

    text = align_left(text)
    maxlen = 0
    for line in text:
        maxlen = max(maxlen, len(line))

    for i in range(len(text)):
        text[i] = ' '*(maxlen - len(text[i])) + text[i]

    clear()
    print("> 2\n")
    return text


def align_by_width(text: List[str]) -> List[str]:
    """Выравнивает текст по ширине
    (относительно длины самой большой строки)

    :param text: Текст для форматирования
    :type text: List[str]
    :return: Отформатированный текст
    :rtype: List[str]
    """

    text = align_left(text)
    maxlen = 0
    for line in text:
        maxlen = max(maxlen, len(line))

    for i in range(len(text)):
        target_spaces = maxlen-len(text[i])
        space_count = text[i].count(" ")
        if space_count:
            expansion = target_spaces//space_count+1

            text[i] = text[i].replace(" ", " "*expansion)
            text[i] = text[i].replace(
                " "*expansion,
                " "*(expansion + 1),
                target_spaces % space_count
            )

    clear()
    print("> 3\n")
    return text


def detect_align(text: List[str]) -> Callable:
    """Возвращает функцию для форматирования, 
    соответствующую текущему типу форматирования 
    текста 

    :param text: Текст для форматирования
    :type text: List[str]
    :return: функция для форматирования
    :rtype: Callable
    """

    if any(text[i][0] == ' ' for i in range(len(text))):
        return align_right
    elif all(len(text[i]) == len(text[i+1]) for i in range(len(text)-1)):
        return align_by_width
    return align_left


def delete_word(text: List[str]) -> List[str]:
    """Осуществляет ввод слова и удаляет 
    все вхождения введённого слова из текста

    :param text: Текст для форматирования
    :type text: List[str]
    :return: Отформатированный текст
    :rtype: List[str]
    """
    output_text(text)
    print()
    removal_word = fi.param_input(
        str,
        r'[a-zA-Zа-яА-Я]+',
        custom_prompt="Введите слово для удаления: "
    )

    formatting = detect_align(text)

    for i in range(len(text)):
        word_list = text[i].split()

        for j in range(len(word_list)):
            if removal_word in word_list[j] and re.fullmatch(
                f'[.,?!:;\'"]?{removal_word}[.,?!:;\'"]?',
                word_list[j]
            ):

                removal = ''
                if word_list[j][0] in '.,?!:;\'"':
                    removal = word_list[j][0] + removal
                if word_list[j][-1] in '.,?!:;\'"':
                    removal += word_list[j][-1]
                word_list[j] = removal

            else:
                word_list[j] = ' ' + word_list[j]

        text[i] = ''
        for word in word_list:
            text[i] += word

    text = formatting(text)

    clear()
    print(f"> 4 : {removal_word}\n")
    return text


def replace_word(text: List[str]) -> List[str]:
    """Осуществляет ввод слов для замены
    и заменяет одно слово другим во всём тексте

    :param text: Текст для форматирования
    :type text: List[str]
    :return: Отформатированный текст
    :rtype: List[str]
    """
    output_text(text)
    print()
    word_to_replace = fi.param_input(
        str,
        r'[a-zA-Zа-яА-Я]+',
        custom_prompt="Введите слово, которое нужно заменить: "
    )
    print()
    replacement = fi.param_input(
        str,
        r'[a-zA-Zа-яА-Я]+',
        custom_prompt="Введите подстроку, на которую нужно заменять: "
    )

    formatting = detect_align(text)

    for i in range(len(text)):
        word_list = text[i].split()

        for j in range(len(word_list)):
            if word_to_replace in word_list[j]:
                if re.fullmatch(f'[.,?!:;\'"]?{word_to_replace}[.,?!:;\'"]?', word_list[j]):
                    tmp_replacement = replacement
                    if word_list[j][0] in '.,?!:;\'"':
                        tmp_replacement = word_list[j][0] + tmp_replacement
                    if word_list[j][-1] in '.,?!:;\'"':
                        tmp_replacement += word_list[j][-1]
                    word_list[j] = tmp_replacement
            word_list[j] = ' ' + word_list[j]

        text[i] = ''
        for word in word_list:
            text[i] += word

    text = formatting(text)

    clear()
    print(f"> 5 : {word_to_replace} -> {replacement}\n")
    return text


def do_math(text: List[str]) -> List[str]:
    """Выполняет операции сложения и вычитания с числами в тексте

    :param text: Текст для форматирования
    :type text: List[str]
    :return: Отформатированный текст
    :rtype: List[str]
    """
    formatting = detect_align(text)

    for i in range(len(text)):
        while '+' in text[i]:
            halves = text[i].split('+', 1)

        while '-' in text[i]:
            ...

    text = formatting(text)

    clear()
    print(f"> 6\n")
    return text


# far - find_and_remove
def far_longest_word(text: List[str]) -> List[str]:
    """Находит предложение с самым длинным 
    словом в тексте, выводит и удаляет его

    :param text: Текст для форматирования
    :type text: List[str]
    :return: Отформатированный текст
    :rtype: List[str]
    """
    ...


def main():
    text = [
        "— Сорок два! — взвизгнул Лунккуоол. — И это всё, что ты можешь сказать после семи с половиной",
        "миллионов лет работы? — Я всё очень тщательно проверил, — сказал компьютер, — и со всей",
        "определённостью заявляю, что это и есть ответ. Мне кажется, если уж быть с вами абсолютно",
        "честным, то всё дело в том, что вы сами не знали, в чём вопрос. — Но это же великий вопрос! Окончательный",
        "вопрос жизни, Вселенной и всего такого! — почти завыл Лунккуоол. — Да, — сказал компьютер голосом",
        "страдальца, просвещающего круглого дурака. — И что же это за вопрос?",
        "s h"
    ]
    running = True
    commands = {
        1: align_left,
        2: align_right,
        3: align_by_width,
        4: delete_word,
        5: replace_word,
        6: do_math,
        7: far_longest_word
    }

    while running:
        output_text(text)
        print(
            "Меню:",
            "1: Выровнять текст по левому краю",
            "2: Выровнять текст по правому краю",
            "3: Выровнять текст по ширине",
            "4: Удалить все вхождения введённого слова",
            "5: Замена одного слова другим во всём тексте",
            "6: Выполнить операции сложения и вычитания",
            "7: Найти и удалить предложение с самым длинным словом из текста",
            "0: Выход",
            sep='\n',
            end="\n\n"
        )
        command = fi.param_input(
            int, "0<=n<=7", "Введите число от 0 до 7 - комманду\n> ")
        clear()

        if command == 0:
            running = False
        else:
            text = commands[command](text)


if __name__ == "__main__":
    main()
