# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
#
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восем',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(word):
    for key, val in dictionary.items():
        if word == key:
            print(val)
        elif word.lower() == key and word.istitle():
            print(val.capitalize())
    if word.lower() not in dictionary:
        print('None')


num_translate_adv(input('Введите число на английском языке: '))
