#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Ошибка: укажите путь к директории" >&2
    exit 1
fi

directory="$1"

if [ ! -d "$directory" ]; then
    echo "Ошибка: директория '$directory' не существует" >&2
    exit 1
fi

find "$directory" -maxdepth 1 -type f \( -name "*.bak" -o -name "*.tmp" -o -name "*.backup" \) -delete