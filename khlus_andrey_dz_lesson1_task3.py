# Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов»,
# задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.
get_number = int(input('Введите число от 0 до 20: '))
while get_number > 20 or get_number < 0:
    get_number = int(input('Введите число от 0 до 20: '))
if get_number == 1:
    print(get_number, 'процент')
elif 1 < get_number < 5:
    print(get_number, 'процента')
else:
    print(get_number, 'процентов')


for i in range(0, 21):
    if i == 1:
        print(i, 'процент')
    elif 1 < i < 5:
        print(i, 'процента')
    else:
        print(i, 'процентов')
