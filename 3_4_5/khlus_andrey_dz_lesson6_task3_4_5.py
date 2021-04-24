# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между
# значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий
# из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
# что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи

from itertools import zip_longest
import json
import sys

with open('users.csv', 'r', encoding='utf-8') as f1, open('hobby.csv', 'r', encoding='utf-8') as f2:
    get_users = [get.strip('\n') for get in f1.readlines()]
    get_hobby = [get.strip('\n') for get in f2.readlines()]
    if len(get_users) >= len(get_hobby):    # Подскажите на сколько правильно определять число строк в файле через len, а не через сумму единичек?
        users_hobby_dict = {users: hobby for users, hobby in zip_longest(get_users, get_hobby, fillvalue=None)}
    else:
        exit(1)
    print(users_hobby_dict)
    with open('home_work6_3.json', 'w', encoding='utf-8') as f:
        json.dump(users_hobby_dict, f, ensure_ascii=False)
#
# # 4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# # (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# # Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные
# # в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# # Иванов,Иван,Иванович: скалолазание,охота
# # Петров,Петр,Петрович: горные лыжи
#
with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    with open('users.csv', 'r', encoding='utf-8') as f1, open('hobby.csv', 'r', encoding='utf-8') as f2:
        get_users = f1.readline().strip('\n')
        get_hobby = f2.readline().strip('\n')
        if len(get_users) >= len(get_hobby):
            users_hobby_dict = {users: hobby for users, hobby in zip_longest(get_users, get_hobby, fillvalue=None)}
        else:
            exit(1)
        while get_users:
            if len(get_hobby) < len(get_hobby):
                get_hobby = None
            f.write(f'{get_users}: {get_hobby} \n')
            get_users = f1.readline().strip('\n')
            get_hobby = f2.readline().strip('\n')

# Task 5
# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

users, hobby, users_hobby = sys.argv[1:]
with open(users_hobby, 'w', encoding='utf-8') as f:
    with open(users, 'r', encoding='utf-8') as f1, open(hobby, 'r', encoding='utf-8') as f2:
        get_users = f1.readline().strip('\n')
        get_hobby = f2.readline().strip('\n')
        if len(get_users) >= len(get_hobby):
            users_hobby_dict = {users: hobby for users, hobby in zip_longest(get_users, get_hobby, fillvalue=None)}
        else:
            exit(1)
        while get_users:
            if len(get_hobby) < len(get_hobby):
                get_hobby = None
            f.write(f'{get_users}: {get_hobby} \n')
            get_users = f1.readline().strip('\n')
            get_hobby = f2.readline().strip('\n')


