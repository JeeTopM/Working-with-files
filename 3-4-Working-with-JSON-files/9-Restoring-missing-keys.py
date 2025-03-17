"""
Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи, присваивая этим ключам значение null. 
Ключ считается недостающим, если он присутствует в каком-либо другом объекте, но отсутствует в данном. 
Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json.
"""

import json

name = "people.json"
link = "..." + name
with open(link, encoding="utf-8") as file, open('updated_people.json', 'w', encoding='utf-8') as merge:
    rows = json.load(file)
    data = {}
    list_people = []
    for row in rows:
        for key, value in row.items():
            data[key] = data.get(key, None)
    for i in rows:
        list_people.append(data | i)
    json.dump(list_people, merge, ensure_ascii=True, indent=3)



"""
import json


with open('people.json', encoding='utf-8') as js:
    content = json.load(js)

keys = set()
for data in content:
    keys |= data.keys()

for data in content:
    data |= dict.fromkeys(keys - data.keys())

with open('updated_people.json', 'w') as js:
    json.dump(content, js, indent=3)
"""