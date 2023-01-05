
# Втоая часть, взята из вашего решения. Пробовал через f.readline считывать построчно относительно вводимых
# индексов из строки, не получилось!

import sys

item = [4]
with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(item) > 1:
        start_idx = int(item[0])
        end_idx = int(item[1])
    elif len(item) == 0:
        start_idx = 0
        end_idx = sum(1 for line in f)
        f.seek(0)
    else:
        start_idx = int(item[0])
        end_idx = sum(1 for line in f)
        f.seek(0)

    for idx, line in enumerate(f):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())
