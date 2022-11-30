"""Звягин Даниил ИУ7-13Б

Защита лабораторной работы номер 12

Найти в тексте предложение со словом, содержащим наибольшее кол-во гласных букв
"""


# sentence with word with biggest amount of vowels
def find_swwwbaov(text):

    sentence_borders = []
    closed_sentence = True

    for i in range(len(text)):
        for j in range(len(text[i])):
            if closed_sentence:
                sentence_borders.append([[i, j], [None, None]])
                closed_sentence = False
            elif text[i][j] in '.!?':
                sentence_borders[-1][1] = [i, j]
                closed_sentence = True

    senteces = ['']*len(sentence_borders)

    for i, border in enumerate(sentence_borders):
        if border[0][0] == border[1][0]:
            senteces[i] = text[border[0][0]][border[0][1]:border[1][1]+1]
        else:
            senteces[i] = text[border[0][0]][border[0][1]:]

            for j in range(border[0][0]+1, border[1][0]):
                senteces[i] += ' ' + text[j]

            senteces[i] += ' ' + text[border[1][0]][:border[1][1]+1]

    maxcount = 0
    maxindex = 0
    for i, sentence in enumerate(senteces):
        print(sentence_borders[i], sentence)
        for word in sentence.split():
            vowel_count = sum(
                1 if sym in 'яуаеёиоэaeyuio' else 0 for sym in word)
            if vowel_count > maxcount:
                maxcount = vowel_count
                maxindex = i

    return senteces[maxindex]


def main():
    text = [
        "— Сорок два! — взвизгнул Лунккуоол. — И это всё, что ты можешь сказать после",
        "семи с половиной миллионов лет работы? — Я всё очень тщательно проверил, — сказал",
        "компьютер, — и со всей определённостью заявляю, что это и есть ответ. Мне кажется,",
        "если уж быть с вами абсолютно честным, 90+90+1-2 то-всё дело в том, что вы сами не знали,",
        "в чём вопрос. — Но это+же великий вопрос! Окончательный вопрос жизни, Вселенной",
        "и всего такого! — почти 40+2 завыл Лунккуоол. — Да, — сказал компьютер голосом",
        "страдальца, -2+44 просве щающего круглого дурака. — И что 60-18 же это за вопрос?"
    ]

    print("Текст:")
    print(*text, sep='\n')

    target_sent = find_swwwbaov(text)

    print("\nНайденное предложение со словом с наибольшим кол-вом гласных букв:")
    print(target_sent.strip())


if __name__ == '__main__':
    main()
