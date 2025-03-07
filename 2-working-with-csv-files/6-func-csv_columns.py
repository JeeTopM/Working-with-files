"""
Функция csv_columns()

Реализуйте функцию csv_columns(), которая принимает один аргумент:
filename — название csv файла, например, data.csv
Функция должна возвращать словарь, в котором ключом является название столбца файла filename, 
а значением — список элементов этого столбца.
"""

import csv


def csv_columns(filename):

    with open(filename, encoding="utf-8") as csv_file:
        rows = csv.DictReader(csv_file)
        data = {}
        for row in rows:
            for key in list(row.keys()):
                data[key] = data.get(key, []) + [row[key]]
        return data


name = input("Укажите путь к файлу: ")
print(csv_columns(name))


# Какое хорошее решение...
'''
import csv

def csv_columns(filename):

    with open(filename, encoding="utf-8") as file_in:
        rows = list(csv.reader(file_in))
        return {key: value for key, *value in zip(*rows)}
'''