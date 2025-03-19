"""
Количество файлов

Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит единственное число — количество файлов в этом архиве.
"""

from zipfile import ZipFile

link = "/Users/lev/Documents/Programming/Python/workbook.zip"
with ZipFile(link) as zip_file:
    info = zip_file.infolist()
    print(sum(not i.is_dir() for i in info))

'''
with ZipFile(link) as zip_file:
    info = zip_file.namelist()
    cht = 0
    for i in info:
        if i.endswith('/'):
            pass
        else:
            cht += 1
    print(cht)
'''
