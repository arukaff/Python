#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Использование: $0 <директория>" >&2
    exit 1
fi

target_dir="$1"

if [ ! -d "$target_dir" ]; then
    echo "Ошибка: директория '$target_dir' не существует" >&2
    exit 1
fi

find "$target_dir" -maxdepth 1 -type f -print0 | while IFS= read -r -d '' file; do
    owner=$(stat -c "%U" "$file")
    dest_dir="$target_dir/$owner"
    mkdir -p "$dest_dir"
    if cp --preserve=all "$file" "$dest_dir/"; then
        chown "$owner" "$dest_dir/$(basename "$file")" 2>/dev/null || echo "Предупреждение: не удалось установить владельца для файла '$file'. Требуются права root." >&2
    else
        echo "Ошибка при копировании файла '$file'" >&2
    fi
done