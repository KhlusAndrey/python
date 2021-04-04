# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Ваедите продолжительность в секундах: '))

hour = (duration // 3600) % 24
minute = (duration // 60) % 60
second = duration % 60
day = duration // 86400

if day == 0:
    print(hour, 'час', minute, 'мин', second, 'сек', sep=' ')
else:
    print(day, 'дн', hour, 'час', minute, 'мин', second, 'сек', sep=' ')
