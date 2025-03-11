"""
Лог-файл

Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. 
В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты, в третьем — дата и время изменения. 
При этом email пользователь менять не может, только имя:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...
Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для каждого пользователя 
и записывает их в файл new_name_log.csv. 
В файле new_name_log.csv первой строкой должны быть заголовки столбцов такие же, как в файле name_log.csv. 
Логи в итоговом файле должны быть расположены в лексикографическом порядке названий электронных ящиков пользователей.
"""

import csv
from datetime import datetime

with open('name_log.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file)
    d = {}
    for row in rows:
        dt = datetime.strptime(row['dtime'], '%d/%m/%Y %H:%M')
        if row['email'] not in d:
            d[row['email']] = row['username'], dt
        else:
            if d[row['email']][-1] < dt:
                d[row['email']] = row['username'], dt

with open("new_name_log.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["username", "email", "dtime"])
    for email, (username, dtime) in sorted(d.items()):
        writer.writerow([username, email, datetime.strftime(dtime, '%d/%m/%Y %H:%M')])            