"""
Спортивные площадки

Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. 
В первом столбце записан тип площадки,  во втором — административный округ, в третьем — название района, в четвертом — адрес:

ObjectName;AdmArea;District;Address
Парк, озелененная городская территория «Лианозовский парк культуры и отдыха»;Северо-Восточный административный округ;район Лианозово;Угличская улица, дом 13
...

Напишите программу, создающую JSON-объект, ключом в котором является административный округ, а значением — JSON-объект, 
в котором, в свою очередь, ключом является название района, относящийся к этому административному округу, 
а значением — список адресов всех площадок в этом районе. Полученный JSON-объект программа должна записать в файл addresses.json.
"""

import json
import csv

name = "playgrounds.csv"
link = "..." + name

with open(link, encoding="utf-8") as csv_file, open(
    "addresses.json", "w", encoding="utf-8"
) as js_file:
    datas = csv.DictReader(csv_file, delimiter=";")
    districts = {}
    for data in datas:
        districts.setdefault(data["AdmArea"], {}).setdefault(
            data["District"], []
        ).append(data["Address"])
    json.dump(districts, js_file, ensure_ascii=False, indent=3)
