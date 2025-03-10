"""
Wi-Fi Москвы

Вам доступен файл wifi.csv, который содержит данные о городском Wi-Fi Москвы. 
В первом столбце записано название округа, во втором — название района, 
в третьем — адрес, в четвертом — количество точек доступа по этому адресу:

adm_area;district;location;number_of_access_points
Центральный административный округ;район Якиманка;город Москва, улица Серафимовича, дом 5/16;5
Центральный административный округ;район Якиманка;город Москва, Болотная набережная, дом 11, строение 1;2
...
Напишите программу, которая определяет количество точек доступа в каждом районе Москвы и выводит названия всех районов, 
для каждого указывая соответствующее количество точек доступа, каждое на отдельной строке, в следующем формате:

<название района>: <количество точек доступа>
Названия районов должны быть расположены в порядке убывания количества точек доступа, 
при совпадении количества точек доступа — в лексикографическом порядке.
"""

import csv

# Через DictReader
with open('wifi.csv', encoding='utf-8') as csv_file:
    rows = csv.DictReader(csv_file, delimiter=';')
    data = {}
    for row in rows:
        data[row['district']] = data.get(row['district'], 0) + int(row['number_of_access_points'])
    sorted_wifi = sorted(data, key=lambda x: (-data[x], x))
    for i in sorted_wifi:
        print(f'{i}: {data[i]}')

'''
# Через reader
with open('wifi.csv', encoding='utf-8') as csv_file:
    rows = csv.reader(csv_file, delimiter=';')
    next(rows)
    data = {}
    for adm_area, district, location, number_of_access_points in rows:
        data[district] = data.get(district, 0) + int(number_of_access_points)
    sorted_wifi = sorted(data.items(), key=lambda x: (-x[1],x[0]))
    for name, number in sorted_wifi:
        print(f'{name}: {number}')
'''