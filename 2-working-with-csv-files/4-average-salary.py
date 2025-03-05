"""
Средняя зарплата

Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников в различных компаниях. 
В первом столбце записано название компании, а во втором — зарплата очередного сотрудника:

company_name;salary
Atos;135000
ХайТэк;24400
Philax;128600
Инлайн Груп;43900
IBS;70600
Oracle;131600
Atos;91000
...

Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников 
и выводит их названия, каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты, 
они должны быть расположены в лексикографическом порядке их названий.
"""

import csv

with open(
    "/Users/lev/Documents/Programming/Python/Working-with-files/salary_data.csv",
    encoding="utf-8",
) as csv_file:
    rows = csv.DictReader(csv_file, delimiter=";")
    data = {}
    for row in rows:
        company_name = row["company_name"]
        salary = int(row["salary"])
        if company_name not in data:
            data[company_name] = [salary, 1]
        else:
            data[company_name][0] += salary
            data[company_name][1] += 1

    data2 = {name: total // count for name, (total, count) in data.items()}

    for name_company in sorted(data2, key=data2.get):
        print(name_company)

'''

Не моё, но надо запомнить


import csv

d = {}
with open('salary_data.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    for key, value in rows[1:]:
        d[key] = d.get(key, []) + [int(value)]

    d_sort = sorted(d, key=lambda x: (sum(d[x]) / len(d[x]), x))
    print(*d_sort, sep='\n')
'''