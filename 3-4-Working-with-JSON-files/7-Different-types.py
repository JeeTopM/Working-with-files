"""
Разные типы

Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]

Напишите программу, которая создает список, элементами которого являются объекты из списка, 
содержащегося в файле data.json, измененные по следующим правилам:
- если объект является строкой, в его конец добавляется восклицательный знак
- если объект является числом, он увеличивается на единицу
- если объект является логическим значением, он инвертируется
- если объект является списком, он удваивается
- если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
- если объект является пустым значением (null), он не добавляется

Полученный список программа должна записать в файл updated_data.json.
"""

import json

with open("data.json", encoding="utf-8") as file:
    data = json.load(file)

json_data = []
for i in data:
    if isinstance(i, str):
        json_data.append(i + "!")
    elif isinstance(i, bool):
        json_data.append(not i)
    elif isinstance(i, int):
        json_data.append(i + 1)
    elif isinstance(i, list):
        json_data.append(i + i)
    elif isinstance(i, dict):
        i.update(newkey=None)
        json_data.append(i)
    else:
        pass
with open("updated_data.json", "w", encoding="utf-8", newline="") as file:
    json.dump(json_data, file, ensure_ascii=True, indent=3)

'''
import json as js

with open("data.json", encoding="utf-8") as file, open(
    "updated_data.json", "w", encoding="utf-8"
) as out:
    d = {
        str: lambda x: x + "!",
        int: lambda x: x + 1,
        bool: lambda x: bool(abs(x - 1)),
        list: lambda x: x * 2,
        dict: lambda x: x | {"newkey": None},
    }
    js.dump([(x := (d[type(i)])(i)) for i in js.load(file) if not i is None], out)
'''