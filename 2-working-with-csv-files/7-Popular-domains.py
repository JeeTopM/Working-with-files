"""
Популярные домены

Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса. 
В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...
Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...
где в первом столбце записано название почтового домена, а во втором — количество пользователей, 
использующих данный домен. Домены в файле должны быть расположены в порядке возрастания количества их использований, 
при совпадении количества использований — в лексикографическом порядке.
"""

import csv

with open("data-2.csv", encoding="utf-8") as csv_file:
    rows = csv.DictReader(csv_file)
    data = {}
    for row in rows:
        email = row["email"].split("@")[1]
        data[email] = data.get(email, 0) + 1
    sorted_domains = sorted(data.items(), key=lambda x: (x[1], x[0]))

with open("domain_usage.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["domain", "count"])
    for domain, count in sorted_domains:
        writer.writerow([domain, count])
