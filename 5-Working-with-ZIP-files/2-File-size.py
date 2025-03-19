"""
Объем файлов

Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит суммарный объем файлов этого архива в сжатом и не сжатом видах в байтах, в следующем формате:

Объем исходных файлов: <объем до сжатия> байт(а)
Объем сжатых файлов: <объем после сжатия> байт(а)
"""
from zipfile import ZipFile

link = "/Users/lev/Documents/Programming/Python/workbook.zip"
with ZipFile(link) as zip_file:
    # info = zip_file.namelist()
    # zip_file.printdir()