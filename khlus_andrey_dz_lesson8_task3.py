"""
3.	Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3
>>> a = calc_cube(5)
5: <class 'int'>
"""
from functools import wraps


def type_logger(func):
    def wrapper(x):
        print(f'{x} : {type(x)}')
        return func(x)
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)


"""
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in args:
            print(f'{func.__name__}({i} : {type(i)})')
        return func(*args)
    return wrapper


@type_logger
def calc_cube(*args):
    calc = [x ** 3 for x in args]
    return calc


b = calc_cube(5, 7)
# print(b)
# print(calc_cube.__name__)
