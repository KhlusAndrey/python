# 4.	Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
from time import perf_counter
from sys import getsizeof

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

start0 = perf_counter()
result0 = [src[i+1] for i in range(len(src) - 1) if src[i] < src[i+1]]
end0 = perf_counter()
print(result0, getsizeof(result0), end0 - start0)

start = perf_counter()
result = [k for i, k in zip(src, src[1:]) if k > i]
end = perf_counter()
print(result, getsizeof(result), end - start)
