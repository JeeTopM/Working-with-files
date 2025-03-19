"""
Избранные

Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит названия файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. 
Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.
"""

from zipfile import ZipFile
from datetime import *

file_path = "/Users/lev/Documents/Programming/Python/workbook.zip"
with ZipFile(file_path) as zip_file:
    zip_list = zip_file.infolist()
    data = []
    for file in zip_list:
        if not file.is_dir():
            dt = datetime(*file.date_time)
            currect_dt = '2021-11-30 14:22:00'
            if dt >= datetime.strptime(currect_dt, '%Y-%m-%d %H:%M:%S'):
                if "/" in file.filename:
                    ind = file.filename.index("/") + 1
                    data.append(file.filename[ind:])
                else:
                    data.append(file.filename)
    print(*sorted(data), sep='\n')
    