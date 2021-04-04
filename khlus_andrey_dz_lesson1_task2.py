# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#      Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
#      Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
#      сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

summa_cube_odd_numbers = []
summa = 0

# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:

# for i in range(100):
#     if i % 2 != 0:
#         i = i**3
#         cube_odd_numbers.append(i)

cube_odd_numbers = [i**3 for i in range(1000) if i % 2 != 0]
print(cube_odd_numbers, len(cube_odd_numbers))

# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#      Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
#      Внимание: использовать только арифметические операции!

for i in range(len(cube_odd_numbers)):
    while cube_odd_numbers[i] > 0:
        digit = cube_odd_numbers[i] % 10
        summa += digit
        cube_odd_numbers[i] = cube_odd_numbers[i] // 10
    if summa % 7 == 0:
        summa_cube_odd_numbers.append(summa)
    summa = 0
print(summa_cube_odd_numbers, len(summa_cube_odd_numbers))

# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
#      сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

for i in range(len(summa_cube_odd_numbers)):
    summa_cube_odd_numbers[i] += 17
    while summa_cube_odd_numbers[i] > 0:
        digit = summa_cube_odd_numbers[i] % 10
        summa += digit
        summa_cube_odd_numbers[i] = summa_cube_odd_numbers[i] // 10
    if summa % 7 == 0:
        summa_cube_odd_numbers[i] = summa
#    summa_cube_odd_numbers.pop(i)
    summa = 0
print(summa_cube_odd_numbers, len(summa_cube_odd_numbers))
