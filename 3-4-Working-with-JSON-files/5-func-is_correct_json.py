"""
Функция is_correct_json()

Реализуйте функцию is_correct_json(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать True, если строка string удовлетворяет формату JSON, или False в противном случае.
"""

import json


def is_correct_json(string):
    pass






# test 1
data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
print(is_correct_json(data))
# test 2
print(is_correct_json("number = 17"))
