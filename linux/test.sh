#!/bin/bash

echo Вас приветствует утилита тестирования скриптов сравнения файлов
echo Вам будут показаны реультаты работы скриптов в разных ситуациях
echo

echo Нажмите Enter, чтобы начать тестирование скриптов по варианту 2
read
clear
bash ./test/test_var2.sh

echo Нажмите Enter, чтобы начать тестирование скриптов по варианту 3
read
clear
bash ./test/test_var3.sh

echo Нажмите Enter, чтобы начать тестирование скриптов по варианту 4
read
clear
bash ./test/test_var4.sh
