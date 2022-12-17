#!/bin/bash

if [ ! -f $1 ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка: файл 1 не найден!
    fi
    exit 42
fi
if [ ! -f $2 ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка: файл 2 не найден!
    fi
    exit 42
fi
if [ -r $1 ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка: недостаточно прав для доступа к файлу 1!
    fi
    exit 42
fi
if [ -r $2 ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка: недостаточно прав для доступа к файлу 2!
    fi
    exit 42
fi

old_IFS=$IFS
IFS=" "

numbers_in_text1=""
text1=$(cat $1)

for word in $text1; do
    num=$(echo "$word" | grep -E "^[+-]?[0-9]+\.[0-9]+$")
    if [ ! -z "$num" ]; then
        numbers_in_text1="$numbers_in_text1 $num"
    fi
done

if [ -z "$numbers_in_text1" ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка: В файле 1 нет ЧПТ!
    fi
    IFS=$old_IFS
    exit 42
fi

numbers_in_text2=""
text2=$(cat $2)

for word in $text2; do
    num=$(echo "$word" | grep -E "^[+-]?[0-9]+\.[0-9]+$")
    if [ ! -z "$num" ]; then
        numbers_in_text2="$numbers_in_text2 $num"
    fi
done

if [ -z "$numbers_in_text2" ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка: В файле 2 нет ЧПТ!
    fi
    IFS=$old_IFS
    exit 42
fi

IFS=$old_IFS

# echo $numbers_in_text1
# echo $numbers_in_text2

if [ "$numbers_in_text1" = "$numbers_in_text2" ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Файлы одинаковые
    fi
    exit 0
else
    if echo "$3" | grep -Eq "^-v$"; then
        echo Файлы разные
    fi
    exit 1
fi
