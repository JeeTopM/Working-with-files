"""
Бассейны
Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, которые открыты в понедельник в период с 10:00 до 12:00. 
Также ему нравится плавать по длинным дорожкам, поэтому из всех работающих в это время бассейнов нужно выбрать бассейн 
с наибольшей длиной дорожки, при равных значениях — c наибольшей шириной.
Вам доступен файл pools.json, содержащий список JSON-объектов, которые представляют данные о крытых плавательных бассейнах:

Под «бассейном» будем подразумевать один JSON-объект из этого списка. У бассейна имеются следующие атрибуты:
* ObjectName — название, будь то фитнес клуб или спортивный комплекс
* AdmArea — административный округ
* District — название района
* Address — адрес
* WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
* DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина, Width — ширина, Depth — глубина

Напишите программу, которая определяет бассейн, подходящий Тимуру. Программа должна вывести его размеры и адрес в следующем формате:
<длина>x<ширина>
<адрес>
"""

import json
from datetime import *

link = "/Users/lev/Documents/Programming/Python/pools.json"

with open(link, encoding="utf-8") as js:
    data = json.load(js)

    dtp = datetime.strptime
    pattern = "%H:%M"

    pools = {}
    for object in data:
        if object["DimensionsSummer"]["Length"] >= 25:
            if object["WorkingHoursSummer"]["Понедельник"]:
                start, stop = object["WorkingHoursSummer"]["Понедельник"].split("-")
                dstart, dstop = dtp(start, pattern), dtp(stop, pattern)
                if dstart <= dtp("10:00", pattern) and dstop >= dtp("12:00", pattern):
                    pools.setdefault(object["DimensionsSummer"]["Length"], []).append(
                        [object["Address"], object["DimensionsSummer"]]
                    )

    max_length = max(pools.keys())
    max_length_pools = pools[max_length]
    widest_pool = max(max_length_pools, key=lambda x: x[1]["Width"])

    length, width = widest_pool[1]["Length"], widest_pool[1]["Width"]
    address = widest_pool[0]
    print(f"{length}x{width}\n{address}")
    # print(f'{widest_pool[1]['Length']}x{widest_pool[1]['Width']}', f'{widest_pool[0]}', sep='\n')


"""
from datetime import timedelta as td

with open('pools.json', encoding='utf-8') as file:
    ft = lambda x: td(hours=int(x.removesuffix(':00')))
    a, b, address, l, w, ds = td(hours=10), td(hours=12), '', 0, 0, 'DimensionsSummer'
    for i in sorted(__import__('json').load(file), key=lambda x: x[ds]['Width']):
        s, f = i['WorkingHoursSummer']['Понедельник'].split('-')
        if ft(s) <= a and ft(f) >= b and i[ds]['Length'] >= l:
            address, l, w = i['Address'],i[ds]['Length'], i[ds]['Width']
    print(f'{l}x{w}\n{address}')
"""
