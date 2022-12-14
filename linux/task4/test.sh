#!/bin/bash

echo Вариант 4 - сравнение ЧПТ в файлах с поддержкой записи типа 1e10

echo Работа скрипта будет произведена с флагом -v
echo После каждого теста будет выводиться значение переменной \$?
echo Нажмите Enter, чтобы начать
read

clear
echo Тест 1 - базовая работа программы - файлы совпадают
echo Файл 1:
cat "./tests/text1.txt"
echo
echo Файл 2:
cat "./tests/text1.txt"
echo

bash ./comparator4.sh "./tests/text1.txt" "./tests/text1.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 2 - первого файла не существует \(аналогично для файла 2\)
echo
bash ./comparator4.sh "./tests/unexisting_stuff.txt" "./tests/text1.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 3 - файлы разные
echo Файл 1:
cat "./tests/text1.txt"
echo
echo Файл 2:
cat "./tests/text2.txt"
echo

bash ./comparator4.sh "./tests/text1.txt" "./tests/text2.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 4 - Числа без \'e\' в записи
echo Файл 1:
cat "./tests/text3.txt"
echo
echo Файл 2:
cat "./tests/text3.txt"
echo

bash ./comparator4.sh "./tests/text3.txt" "./tests/text3.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 5 - Проверка совместимости разных записей чисел
echo Отмечу, что 1.34e2 не будет равно 134.0, как и требовалось в условиях
echo работы. Здесь показываю отсутствие выхода с ошибкой.
echo Файл 1:
cat "./tests/text1.txt"
echo
echo Файл 2:
cat "./tests/text3.txt"
echo

bash ./comparator4.sh "./tests/text1.txt" "./tests/text3.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 6 - Нет ЧПТ в файле 2 \(аналогично для файла 1\)
echo Файл 1:
cat "./tests/text3.txt"
echo
echo Файл 2:
cat "./tests/text4.txt"
echo

bash ./comparator4.sh "./tests/text3.txt" "./tests/text4.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 7 - Для демонстрации уберу слово pluck
echo Файл 1:
cat "./tests/text1.txt"
echo
echo Файл 2:
cat "./tests/text5.txt"
echo

bash ./comparator4.sh "./tests/text1.txt" "./tests/text5.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 8 - разные формы записи чисел в одном файле
echo Файл 1:
cat "./tests/text6.txt"
echo
echo Файл 2:
cat "./tests/text6.txt"
echo

bash ./comparator4.sh "./tests/text6.txt" "./tests/text6.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 9 - проверка на корректность работы
echo Файл 1:
cat "./tests/text5.txt"
echo
echo Файл 2:
cat "./tests/text6.txt"
echo

bash ./comparator4.sh "./tests/text5.txt" "./tests/text6.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тестирование варианта 4 завершено.
echo Нажмите Enter, чтобы выйти
read
