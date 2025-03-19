"""
Форматированный вывод

Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит названия всех файлов из этого архива в лексикографическом порядке, 
указывая для каждого его дату изменения, а также объем до и после сжатия, в следующем формате:

<название файла>
  Дата модификации файла: <дата изменения>
  Объем исходного файла: <объем до сжатия> байт(а)
  Объем сжатого файла: <объем после сжатия> байт(а)
Между данными о двух файлах должна располагаться пустая строка.
"""

from zipfile import ZipFile
from datetime import datetime

file_path = "/Users/lev/Documents/Programming/Python/workbook.zip"
with ZipFile(file_path) as zip_file:
    data = [
        (f.filename.split("/")[-1], datetime(*f.date_time), f.compress_size, f.file_size)
        for f in zip_file.infolist()
        if not f.is_dir()
    ]
    for numb, (name, dt, c_size, f_size) in enumerate(sorted(data)):
        print(f'''{name}\n  Дата модификации файла: {dt}
  Объем исходного файла: {f_size} байт(а)
  Объем сжатого файла: {c_size} байт(а)''')
        if len(data) > numb + 1:
            print()