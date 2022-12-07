#!/bin/bash

if [ ! -f $1 ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка: файл 1 не найден!
    fi
    exit 1
fi
if [ ! -f $2 ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка: файл 2 не найден!
    fi
    exit 1
fi

old_IFS=$IFS
IFS=" "

text1_after_sub=""
flag=""
text1=$(cat "$1")

for word in $text1; do
    if [ -z $flag ]; then
        if echo "$word" | grep -Eq "string:"; then
            flag="true"
            text1_after_sub="$(echo "$word" | grep -Eo "string:.*")"
        fi
    else
        text1_after_sub="$text1_after_sub $word"
    fi
done

if [ -z $flag ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! В первом файле не найдено подстроки \"string:\"
    fi
    exit 1
fi

text2_after_sub=""
flag=""
text2=$(cat "$2")

for word in $text2; do
    if [ -z $flag ]; then
        if echo "$word" | grep -Eq "string:"; then
            flag="true"
            text2_after_sub="$(echo "$word" | grep -Eo "string:.*")"
        fi
    else
        text2_after_sub="$text2_after_sub $word"
    fi
done

if [ -z $flag ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! Во втором файле не найдено подстроки \"string:\"
    fi
    exit 1
fi

if [ "$text1_after_sub" = "$text2_after_sub" ]; then
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

IFS=$old_IFS
