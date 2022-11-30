"""Звягин Даниил ИУ7-13Б
Лабораторная работа номер 12

Тексторый процессор
============================
"""
import os
import re
import fast_inputs as fi
from typing import List, Callable


"""Дуглас Адамс - Автостопом по галактике

— Сорок два! — взвизгнул Лунккуоол. — И это всё, что ты можешь 
сказать после семи с половиной миллионов лет работы?

— Я всё очень тщательно проверил, — сказал компьютер, — и со всей 
определённостью заявляю, что это и есть ответ. 
Мне кажется, если уж быть с вами абсолютно честным, то всё дело в том, 
что вы сами не знали, в чём вопрос.

— Но это же великий вопрос! Окончательный вопрос жизни, Вселенной 
и всего такого! — почти завыл Лунккуоол.

— Да, — сказал компьютер голосом страдальца, просвещающего круглого 
дурака. — И что же это за вопрос?
"""


def clear():
    """Очищает экран"""
    os.system('cls' if os.name == 'nt' else 'clear')


def output_text(text: List[str]):
    """Выводит текст

    :param text: Текст для вывода
    :type text: List[str]
    """
    if not text:
        print("Ого! Кажется от текста совсем ничего не осталось!")
        print("Да... Печальное положение, печальное...")
        print("Что ж, наверное мне стоит выключить программу,")
        print("пока вы не вызвали ошибку в какой-нибудь функции...")
        print("Спасибо, что пользовались и хорошего дня!")
        exit(0)
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
        cursor_pos = 0
        # Длина текста может меняться в процессе выполнения, поэтому range не подходит
        while cursor_pos < len(text[i]):
            if text[i][cursor_pos] in '+-':
                left_arg = ''
                found_flag = False
                min_k = cursor_pos
                for k in range(cursor_pos-1, -1, -1):
                    if text[i][k] == ' ':
                        # if not found_flag:
                        #     continue
                        # else:
                        break

                    if text[i][k] == '-':
                        if not left_arg:
                            break
                        else:
                            left_arg = text[i][k] + left_arg
                            min_k = k
                            continue

                    if text[i][k] in '0123456789':
                        found_flag = True
                        left_arg = text[i][k] + left_arg
                    else:
                        break

                    min_k = k

                if not left_arg:
                    cursor_pos += 1
                    continue

                max_k = cursor_pos
                found_flag = False
                right_arg = ''
                for k in range(cursor_pos+1, len(text[i])):
                    if text[i][k] == ' ':
                        # if not found_flag:
                        #     continue
                        # else:
                        break

                    if text[i][k] in '0123456789':
                        found_flag = True
                        right_arg += text[i][k]
                    else:
                        break

                    max_k += 1

                if not right_arg:
                    cursor_pos += 1
                    continue

                if text[i][cursor_pos] == '+':
                    result = str(int(left_arg) + int(right_arg))
                else:
                    result = str(int(left_arg) - int(right_arg))

                text[i] = text[i][:min_k] + result + text[i][max_k+1:]
                cursor_pos = min_k

            cursor_pos += 1

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
    # сначала найдём границы предложений
    formatting = detect_align(text)
    text = align_left(text)

    sentence_borders = []

    complete_sent_flag = True
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] != ' ' and complete_sent_flag:
                complete_sent_flag = False
                sentence_borders.append([[i, j], [None, None]])
            elif text[i][j] in ".!?":
                sentence_borders[-1][1] = [i, j]
                complete_sent_flag = True

    sentences = [0]*len(sentence_borders)

    for i, sentence_border in enumerate(sentence_borders):
        if sentence_border[0][0] == sentence_border[1][0]:
            sentences[i] = text[sentence_border[0][0]
                                ][sentence_border[0][1]:sentence_border[1][1]+1]
        else:
            sentences[i] = text[sentence_border[0]
                                [0]][sentence_border[0][1]:] + ' '
            for k in range(sentence_border[0][0]+1, sentence_border[1][0]):
                sentences[i] += text[k] + ' '
            sentences[i] += text[sentence_border[1]
                                 [0]][:sentence_border[1][1]+1]

    maxlen = 0
    max_index = 0
    for i, sentence in enumerate(sentences):
        for word in sentence.split():
            if '+' in word:
                subwords = word.split('+')
                for subword in subwords:
                    if len(subword) > maxlen:
                        maxlen = len(subword)
                        max_index = i
                continue
            if len(word) > maxlen:
                maxlen = len(word)
                max_index = i

    if sentence_borders[max_index][0][0] == sentence_borders[max_index][1][0]:
        text[sentence_borders[max_index][0][0]] =\
            text[sentence_borders[max_index][0][0]
                 ][:sentence_borders[max_index][0][1]] +\
            text[sentence_borders[max_index][0][0]
                 ][sentence_borders[max_index][1][1]+1:]

    else:
        text[sentence_borders[max_index][0][0]] =\
            text[sentence_borders[max_index][0]
                 [0]][:sentence_borders[max_index][0][1]]

        text[sentence_borders[max_index][1][0]] =\
            text[sentence_borders[max_index][1]
                 [0]][sentence_borders[max_index][1][1]+1:]

        for k in range(sentence_borders[max_index][1][0]-1,
                       sentence_borders[max_index][0][0], -1):
            text.pop(k)

    for i in range(len(text)-1, -1, -1):
        if not text[i]:
            text.pop(i)

    text = formatting(text)

    clear()
    print(f"> 7")
    print(sentences[max_index], '\n')
    return text


def main():
    text = [
        "— Сорок два! — взвизгнул Лунккуоол. — И это всё, что ты можешь сказать после",
        "семи с половиной миллионов лет работы? — Я всё очень тщательно проверил, — сказал",
        "компьютер, — и со всей определённостью заявляю, что это и есть ответ. Мне кажется,",
        "если уж быть с вами абсолютно честным, 90+90+1-2 то-всё дело в том, что вы сами не знали,",
        "в чём вопрос. — Но это+же великий вопрос! Окончательный вопрос жизни, Вселенной",
        "и всего такого! — почти 40+2 завыл Лунккуоол. — Да, — сказал компьютер голосом",
        "страдальца, -2+44 просвещающего круглого дурака. — И что 60-18 же это за вопрос?"
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
    try:
        main()
    except KeyboardInterrupt:
        print("\nВсего доброго")
        exit(0)
