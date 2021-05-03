# 4.	Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
# (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os


file_size_range = dict.fromkeys([10**i for i in range(1, 9)], 0)
files_size = []
folder = 'some_data'

for root, dirs, files in os.walk(folder):
    for file in files:
        f_path = os.path.join(root, file)
        files_size.append(os.stat(f_path).st_size)

for i in files_size:
    file_size_range[10 ** len(str(i))] += 1

print(file_size_range)
