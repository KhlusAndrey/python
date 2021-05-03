# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

path_dir = r'C:\Users\Admin\Desktop\Geek\Четверть#1\Основы языка Python\Lesson#7'
name_project = 'my_project'
folders_name = ['settings', 'mainapp', 'adminapp', 'authapp']
# folders_list = [['settings', [['set2', []]]], ['mainapp', []], ['adminapp', []], ['authapp', []]]


def make_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print(f'{path} Папка уже существует')


project_path = os.path.join(path_dir, name_project)
make_folder(project_path)
for i in folders_name:
    folder = os.path.join(project_path, i)
    make_folder(folder)

# def make_structured_folder(path, folder_list):
#     """
#     создание структуры folder_list папок со вложенными папками через рекурсию.
#     :param path: путь к месту создания стартера
#     :param folder_list: Структура имен вложенных папок
#     """
#     if folder_list:
#         for i in folder_list:
#             name = i[0]
#             path_fold = os.path.join(path, name)
#             make_folder(path_fold)
#             make_structured_folder(path_fold, i[1])




# make_structured_folder(project_path, folders_list)
