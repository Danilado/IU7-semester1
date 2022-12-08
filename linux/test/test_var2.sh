#!/bin/bash

echo Вариант 2 - сравнение файлов после вхождения подстроки \"string:\"
echo Тестровочные файлы:
echo

echo Файл 1:
cat "./test/var2/text1.txt"
echo
echo Файл 2:
cat "./test/var2/text2.txt"
echo
echo Файл 3:
cat "./test/var2/text3.txt"
echo
echo Файл 4:
cat "./test/var2/text4.txt"
echo
echo Файл 5:
cat "./test/var2/text5.txt"
echo
echo Файл 6:
cat "./test/var2/text6.txt"
echo
echo Файл 7:
cat "./test/var2/text7.txt"
echo

echo Работа скрипта будет произведена с флагом -v
echo После каждого теста будет выводиться значение переменной \$?
echo Тест 1 - базовая работа программы - файлы совпадают
echo Файлы 1 и 2
echo

bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/text2.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

echo Тест 2 - первого файла не существует
echo
bash ./comparator2.sh "./test/var2/unexisting_stuff.txt" "./test/var2/text2.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

echo Тест 3 - второго файла не существует
echo
bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/unexisting_stuff.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

echo Тест 4 - файлы разные
echo Файлы 1 и 3
echo
bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/text3.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

echo Тест 5 - отличие до подстроки \"string:\"
echo Файлы 1 и 4
echo
bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/text4.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

echo Тест 6 - во втором файле нет подстроки \"string:\" \(аналогично для первого\)
echo Файлы 1 и 5
echo
bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/text5.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

echo Тест 7 - отличие в количестве пробельных символов
echo Файлы 1 и 6
echo
bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/text6.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

echo Тест 8 - Подстрока \"string:\" в конце строки
echo Файлы 7 и 7
echo
bash ./comparator2.sh "./test/var2/text7.txt" "./test/var2/text7.txt" -v
echo Код выхода: "$?"
echo
echo Тестирование варианта 2 завершено.
echo Нажмите Enter, чтобы продолжить
read
