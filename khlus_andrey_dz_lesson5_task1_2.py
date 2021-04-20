# 1.	Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
# 2.	*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


def gen_odd_number(max_number):
    for num in range(1, max_number + 1, 2):
        yield num


odd = gen_odd_number(15)
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
# print(next(odd))

# print(*odd)

max_num = int(input('Введите максимальное число для генерации всех отрицательных чисел: '))
odd_nums = [num for num in range(1, max_num + 1, 2)]
print(odd_nums)
