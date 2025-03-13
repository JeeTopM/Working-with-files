"""
Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, 
причем если пары из первого и второго объектов имеют совпадающие ключи, 
то значение следует взять из второго объекта. 
Полученный JSON-объект программа должна записать в файл data_merge.json.
"""

import json

with open("data1.json", encoding="utf-8") as file_1, open(
    "data2.json", encoding="utf-8"
) as file_2, open("data_merge.json", "w", encoding="utf-8") as merge:
    d_1 = json.load(file_1)
    d_2 = json.load(file_2)
    d_0 = d_1 | d_2
    json.dump(d_0, merge, ensure_ascii=True, indent=3)
