#!/bin/bash

echo Вариант 2 - сравнение файлов после вхождения подстроки \"string:\"
# echo Тестровочные файлы:
# echo

echo Работа скрипта будет произведена с флагом -v
echo После каждого теста будет выводиться значение переменной \$?
echo Нажмите Enter, чтобы начать
read

clear
echo Тест 1 - базовая работа программы - файлы совпадают
echo Файл 1:
cat "./test/var2/text1.txt"
echo
echo Файл 2:
cat "./test/var2/text2.txt"
echo

bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/text2.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 2 - первого файла не существует \(аналогично для файла 2\)
echo
bash ./comparator2.sh "./test/var2/unexisting_stuff.txt" "./test/var2/text2.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 3 - файлы разные
echo Файл 1:
cat "./test/var2/text1.txt"
echo
echo Файл 2:
cat "./test/var2/text3.txt"
echo

bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/text3.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 4 - отличие до подстроки \"string:\"
echo Файл 1:
cat "./test/var2/text1.txt"
echo
echo Файл 2:
cat "./test/var2/text4.txt"
echo

bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/text4.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 5 - во втором файле нет подстроки \"string:\" \(аналогично для первого\)
echo Файл 1:
cat "./test/var2/text1.txt"
echo
echo Файл 2:
cat "./test/var2/text5.txt"
echo

bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/text5.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 6 - отличие в количестве пробельных символов
echo Файл 1:
cat "./test/var2/text1.txt"
echo
echo Файл 2:
cat "./test/var2/text6.txt"
echo

bash ./comparator2.sh "./test/var2/text1.txt" "./test/var2/text6.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 7 - Подстрока \"string:\" в конце строки
echo Файл 1:
cat "./test/var2/text7.txt"
echo
echo Файл 2:
cat "./test/var2/text7.txt"
echo

bash ./comparator2.sh "./test/var2/text7.txt" "./test/var2/text7.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тест 8 - Подстрока \"string:\" в конце файла
echo Файл 1:
cat "./test/var2/text8.txt"
echo
echo Файл 2:
cat "./test/var2/text8.txt"
echo

bash ./comparator2.sh "./test/var2/text8.txt" "./test/var2/text8.txt" -v
echo Код выхода: "$?"
echo
echo Нажмите Enter, чтобы продолжить
read

clear
echo Тестирование варианта 2 завершено.
echo Нажмите Enter, чтобы продолжить
read
