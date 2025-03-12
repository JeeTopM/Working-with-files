"""
Элементы JSON

Напишите программу, которая принимает на вход описание одного объекта в формате JSON и выводит все пары ключ-значение этого объекта.

Формат входных данных
На вход программе подается корректное описание одного объекта в формате JSON.

Формат выходных данных
Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ и значение двоеточием, каждую на отдельной строке. 
Если значением ключа является список, то все его элементы должны быть выведены через запятую.
"""
import sys 
import json

text = sys.stdin.read()
json_file = json.loads(text)

for key, value in json_file.items():
    if isinstance(value, list):
        print(f'{key}: {", ".join(map(str, value))}')
    else:
        print(f"{key}: {value}")




# 1
{"size": 36, "style": "bold", "name": "text1", "alignment": "center"}

# 2
{
 "type": "donut", 
 "name": "Cake", 
 "tastes": ["chocolate", "cream", "strawberry"]
}

# 3
{
"src": "Images/Sun.png",
"name": "sun1",
"hOffset": 250,
"AAA": ["ABC", 123, 123, "XYZ"],
"vOffset": 250,
"alignment": "center",
"key": [1, 2, 3, 4, 5],
"another_key": ["a", "b", "c"]
}