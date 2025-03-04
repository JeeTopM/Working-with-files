import csv

# Как надо:
with open('grades.csv', encoding='utf-8', ) as csv_file:
    # создаем reader объект и указываем в качестве разделителя символ ;
    rows = csv.reader(csv_file, delimiter=';')
    # выводим каждую строку
    for row in rows:
        print(row)

# Было, не работает так
'''
with open('grades.csv', encoding='utf-8', ) as csv_file:
    # считываем содержимое файла
    text = csv_file.read()
    # создаем reader объект и указываем в качестве разделителя символ ;
    rows = csv.reader(text, delimiter=';')
    # выводим каждую строку
    for row in rows:
        print(row)
'''