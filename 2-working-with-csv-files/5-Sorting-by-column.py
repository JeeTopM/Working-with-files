"""
Сортировка по столбцу

Вам доступен файл deniro.csv, каждый столбец которого содержит либо только числа, либо строковые значения:

Machete,2010,72
Marvin's Room,1996,80
Raging Bull,1980,97
...
Напишите программу, которая сортирует содержимое данного файла по указанному столбцу. 
Причем данные должны быть отсортированы в порядке возрастания чисел, если столбец содержит числа, 
и в лексикографическом порядке слов, если столбец содержит слова.

Формат входных данных
На вход программе подается натуральное число — номер столбца файла deniro.csv.

Формат выходных данных
Программа должна отсортировать содержимое файла deniro.csv по введенному столбцу и вывести полученный результат в исходном формате.
"""

import csv

with open(
    "/Users/lev/Documents/Programming/Python/Working-with-files/deniro.csv",
    encoding="utf-8",
) as csv_file:
    
    rows = csv.reader(csv_file)
    list_film = []
    for n in rows:
        list_film.append([n[0], int(n[1]), int(n[2])])
    inp = int(input())
    sort_rows = sorted(list_film, key=lambda x: x[inp - 1])
    for name, year, duration in sort_rows:
        print(f'{name},{year},{duration}')
