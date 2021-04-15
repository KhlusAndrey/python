# 2.	Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

# 3.	*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?

from requests import get
from _datetime import datetime




def currency_rates(code_val=input('Введите код тикер валюты: ').upper()):
    """
    Функция определения курса валюты на текущую дату, с запросом API  http://www.cbr.ru/scripts/XML_daily.asp.
    :param code_val: Необходимо ввести тикер валюты
    """
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    get_data = datetime.strptime((response[response.index('Date="') + len('Date="'):response.index('" name')]), "%d.%m.%Y").date()
    response = response.split('</Valute>')
    for i in response:
        if code_val in i and len(code_val) == 3:
            value = (i[i.index('<Value>') + len('<Value>'):i.index('</Value>')])
            print(f"Курс {code_val} составляет {float(value.replace(',', '.'))} на дату {get_data}")
        elif code_val in i and len(code_val) != 3:
            print(None)


if __name__ == '__main__':
    currency_rates()
