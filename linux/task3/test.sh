#!/bin/bash

echo Вариант 3 - сравнение ЧПТ в файлах

echo Работа скрипта будет произведена с флагом -v
echo После каждого теста будет выводиться значение переменной \$?
echo Нажмите Enter, чтобы начать
read

clear
echo Тест 1 - базовая работа программы - файлы совпадают
echo Файл 1:
cat "/tests/text1.txt"
echo
echo Файл 2:
cat "/tests/text1.txt"
echo

bash ./comparator3.sh "/tests/text1.txt" "/tests/text1.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 2 - первого файла не существует \(аналогично для файла 2\)
echo
bash ./comparator3.sh "/tests/unexisting_stuff.txt" "/tests/text1.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 3 - файлы разные
echo Файл 1:
cat "/tests/text1.txt"
echo
echo Файл 2:
cat "/tests/text2.txt"
echo

bash ./comparator3.sh "/tests/text1.txt" "/tests/text2.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 4 - присутствует ЧПТ в записи типа 1e10
echo Файл 1:
cat "/tests/text4.txt"
echo
echo Файл 2:
cat "/tests/text3.txt"
echo

bash ./comparator3.sh "/tests/text4.txt" "/tests/text3.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 5 - во втором файле нет ЧПТ \(аналогично для первого\)
echo Файл 1:
cat "/tests/text1.txt"
echo
echo Файл 2:
cat "/tests/text7.txt"
echo

bash ./comparator3.sh "/tests/text1.txt" "/tests/text7.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 6 - Числа без точки в файле 1 \(аналогично для файла 2\)
echo Файл 1:
cat "/tests/text5.txt"
echo
echo Файл 2:
cat "/tests/text6.txt"
echo

bash ./comparator3.sh "/tests/text5.txt" "/tests/text6.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 7 - Для демонстрации уберу слово pluck
echo Файл 1:
cat "/tests/text1.txt"
echo
echo Файл 2:
cat "/tests/text8.txt"
echo

bash ./comparator3.sh "/tests/text1.txt" "/tests/text8.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тестирование варианта 3 завершено.
echo Нажмите Enter, чтобы продолжить
read
