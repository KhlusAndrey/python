# 3.	Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

import os
import shutil
test_dir = 'test_templates'
if not os.path.exists(test_dir):
    os.mkdir(test_dir)

folder = r'my_project'
files_list = []

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('.html'):
            files_list.append(os.path.join(root, file))

for path in files_list:
    folder = os.path.join(test_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    path_copy = os.path.join(folder, os.path.basename(path))
    shutil.copy2(path, path_copy)

# Подскажите для чего это условие "обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён)" было в примечании к заданию?