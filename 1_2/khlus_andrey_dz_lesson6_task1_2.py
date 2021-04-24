# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
# 2.*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания. Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.
#
get_log = []
get_spam = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:                             # Подскажите, когда мы запускаем цикл по файлу f он по умолчанию берет
        #line_split = f.readline().split()     # одну строку line до символа \n, и f.readline можно уже не использовать?
        line_split = line.split()              # И почему-то при f.readline по счетчику получается почти в 2 раза меньшие значения количества повторений
        get = (line_split[0], line_split[5], line_split[6]) # ('216.46.173.126', 1173), ('180.179.174.219', 917), ('204.77.168.241', 716), ('65.39.197.164', 682), ('80.91.33.133', 577)
        get_log.append(get)

get_log.sort(key=lambda x: x[0])
print(get_log[:10])

for x, y, z in get_log:
    get_spam.setdefault(x, 0)    # Долго пытался посчитать число вхождений IP через .count(x), так и не получилось.
    get_spam[x] += 1

get_spam = sorted(get_spam.items(), key=lambda x: x[1], reverse=True)
print(get_spam[:10])



