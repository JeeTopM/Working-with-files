"""
Последний день на Титанике

Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник. 
В первом столбце указана единица, если пассажир выжил, и ноль в противном случае, 
во втором столбце записано полное имя пассажира, в третьем — пол, в четвертом — возраст:

survived;name;sex;age
0;Mr. Owen Harris Braund;male;22
1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
...
Напишите программу, которая выводит имена выживших пассажиров, которым было менее 18 лет, 
каждое на отдельной строке. Причем сначала должны быть расположены имена всех пассажиров мужского пола, 
а затем — женского, имена же непосредственно в мужском и женском списках должны быть расположены в своем исходном порядке.
"""

import csv

with open("titanic.csv", encoding="utf-8") as file:
    rows = csv.DictReader(file, delimiter=";")
    data = {"male": [], "female": []}
    for row in rows:
        age = float(row["age"])
        if row["survived"] == "1" and age < 18:
            if row["sex"] == "male":
                data["male"].append(row["name"])
            else:
                data["female"].append(row["name"])
    for child_man in data["male"]:
        print(child_man)
    for child_woman in data["female"]:
        print(child_woman)


"""
# от пользователей, красота
with open('titanic.csv', encoding='utf-8') as file:
    d = {}
    for i in __import__('csv').DictReader(file, delimiter=';'):
        if i['survived'] == '1' and float(i['age']) < 18:
            d[i['name']] = i['sex']
    for i in sorted(d, key=lambda x: d[x], reverse=True):
        print(i)
"""
