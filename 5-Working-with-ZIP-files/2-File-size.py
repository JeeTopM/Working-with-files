"""
Объем файлов

Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит суммарный объем файлов этого архива в сжатом и не сжатом видах в байтах, в следующем формате:

Объем исходных файлов: <объем до сжатия> байт(а)
Объем сжатых файлов: <объем после сжатия> байт(а)
"""
from zipfile import ZipFile

file_path = "/Users/lev/Documents/Programming/Python/workbook.zip"
with ZipFile(file_path) as zip_file:
    info = zip_file.infolist()
    print(f'Объем исходных файлов: {sum(i.file_size for i in info)} байт(а)')
    print(f'Объем сжатых файлов: {sum(i.compress_size for i in info)} байт(а)')