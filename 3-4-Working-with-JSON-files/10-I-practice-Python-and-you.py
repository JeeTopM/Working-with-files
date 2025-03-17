"""
Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о странах и исповедуемых в них религиях
Каждый объект из этого списка содержит два атрибута:
country — страна
religion — исповедуемая религия
Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии, 
а в качестве значения — список стран, в которых исповедуется данная религия. 
Полученный JSON-объект программа должна записать в файл religion.json.
"""

import json

link = "countries.json"
with open(link, encoding="utf-8") as js, open(
    "religion.json", "w", encoding="utf-8"
) as file:
    rows = json.load(js)
    data = {}
    for row in rows:
        data.setdefault(row["religion"], []).append(row["country"])
    json.dump(data, file, ensure_ascii=ascii, indent=3)



"""
import json as js

with open('countries.json', encoding='utf-8') as file, open('religion.json', 'w') as out:
    d = {}
    [d.setdefault(i['religion'], []).append(i['country']) for i in js.load(file)]
    out = js.dump(d, out)
"""