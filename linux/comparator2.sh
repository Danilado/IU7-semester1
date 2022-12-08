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

old_IFS=$IFS
IFS=" "

text1_after_sub=""
flag=""
text1=$(cat "$1")

while read -r line; do
    if [ -z $flag ]; then
        if echo "$line" | grep -Eq "string:"; then
            flag="true"
            text1_after_sub="$(echo "$line" | grep -Eo "string:.*")"
        fi
    else
        text1_after_sub="${text1_after_sub}\n${line}"
    fi
done <$1

if [ -z $flag ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! В первом файле не найдено подстроки \"string:\"
    fi
    IFS=$old_IFS
    exit 42
fi

# echo "$text1_after_sub"

text2_after_sub=""
flag=""
text2=$(cat "$2")

while read -r line; do
    if [ -z $flag ]; then
        if echo "$line" | grep -Eq "string:"; then
            flag="true"
            text2_after_sub="$(echo "$line" | grep -Eo "string:.*")"
        fi
    else
        text2_after_sub="${text2_after_sub}\n${line}"
    fi
done <$2

if [ -z $flag ]; then
    if echo "$3" | grep -Eq "^-v$"; then
        echo Ошибка! Во втором файле не найдено подстроки \"string:\"
    fi
    IFS=$old_IFS
    exit 42
fi

# echo "$text2_after_sub"

IFS=$old_IFS

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
