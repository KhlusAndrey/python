"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
 исключение ValueError, если что-то не так, например:
def val_checker...
    ...
@val_checker(lambda x: x > 0)

def calc_cube(x):
   return x ** 3
>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?
"""
from functools import wraps


def val_checker(arg):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in args:
                if i <= 0:
                    raise ValueError(f'wrong val {i}')
                else:
                    print(f'{args} : {type(args)}')
                    return func(i)
        return wrapper
    return outer


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
# print(a)
# print(calc_cube.__name__)
