"""
Студенты курса
Вам доступен файл students.json, содержащий список JSON-объектов, которые представляют данные о студентах некоторого курса.
Под «студентом» мы будем подразумевать один JSON-объект из этого списка. У студента имеются следующие атрибуты:
* name — имя 
* city — город проживания
* age — возраст
* progress — прогресс по курсу в процентах
* phone— контактный номер
Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:
* возраст 18 лет или более 
* прогресс по курсу 75% или более
Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер), 
и записать в него данные выбранных студентов, расположив их в лексикографическом порядке имён. 
В качестве разделителя в файле data.csv должна быть использована запятая.
"""

import json
import csv

with open("students.json", encoding="utf=8") as js_file, open(
    "data.csv", "w", encoding="utf-8"
) as csv_file:
    data = json.load(js_file)
    students = []
    for student in data:
        if student["age"] >= 18 and student["progress"] >= 75:
            students.append([student["name"], student["phone"]])
    students.sort()
    writer = csv.writer(csv_file)
    writer.writerow(["name", "phone"])
    writer.writerows(students)
