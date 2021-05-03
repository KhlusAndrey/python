"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя
пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
выбросить исключение ValueError.

Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
данном случае использовать функцию re.compile()?

"""

import re
e_mail_name = 'someone88@geekbrains.ru'
e_mail_name_dictionary = {}

# RE_MAIL_NAME = re.compile(r'(^(?P<usernamre>[a-zA-Z\d_.+-]+)@=(?P<domian>[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$))')
RE_MAIL_NAME = re.compile(r'^([a-zA-Z\d_.+-]+)@([a-zA-Z\d-]+\.[a-zA-Z0-9-.]+$)')


def email_parse(e_mail):
    search_email = RE_MAIL_NAME.search(e_mail)
    if search_email:
        get_e_mail_name = RE_MAIL_NAME.findall(e_mail)[0]
        e_mail_name_dictionary['username'] = get_e_mail_name[0]
        e_mail_name_dictionary['domain'] = get_e_mail_name[1]
        print(e_mail_name_dictionary)
    else:
        raise ValueError(f'Неверный адрес {e_mail}')


def email_parse_split(e_mail):
    search_email = RE_MAIL_NAME.search(e_mail)
    if search_email:
        get_e_mail_name = RE_MAIL_NAME.split(e_mail)
        print(get_e_mail_name, len(get_e_mail_name), type(get_e_mail_name))
        e_mail_name_dictionary['username'] = get_e_mail_name[1]
        e_mail_name_dictionary['domain'] = get_e_mail_name[2]
        print(e_mail_name_dictionary)
    else:
        raise ValueError(f'Неверный адрес {e_mail}')
# Почему при split-e у меня появляются два дополнительных значения в list [0],[4] и как их можно убрать? Через
# определение регулярного выражения или только указывать индексы?


email_parse(e_mail_name)
email_parse_split(e_mail_name)

"""
2. *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации
 вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
 например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
Можно ли для них уточнить регулярное выражение?
"""

RE_LOG_WEB = re.compile(r'((?:\d{,3}[.]){3}\d{,3})\W+(\d{1,}/\w+/(?:\d{2,}:){3}\d+\s+\+\d+)\W+([A-Z]+)\s((?:/\w+){2}\s(?:\w+/\d+\.\d+))\W+(\d+)\W+(\d+)')

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        get_findall = RE_LOG_WEB.findall(line)
        print(get_findall)

# Вопрос, почему при findall, мы получаем list из одного элемента, хотя они указываются через ',' и как их можно
# выводить именно списком с элементами, чтобы обращаться по индексам и дополнительно не резать через split?
