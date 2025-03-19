"""
Наилучший показатель

Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит название файла из этого архива, который имеет наилучший показатель степени сжатия.
"""

from zipfile import ZipFile

file_path = "/Users/lev/Documents/Programming/Python/workbook.zip"
with ZipFile(file_path) as zip_file:
    info = zip_file.infolist()
    d = {}
    for i in info:
        if not i.is_dir():
            res = 100 - (i.compress_size / i.file_size * 100)
            if "/" in i.filename:
                ind = i.filename.index("/") + 1
                d.setdefault(i.filename[ind:], []).append(res)
            else:
                d.setdefault(i.filename, []).append(res)

    print(max(d, key=d.get))


"""
from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    filelist = zip_file.infolist()
    t = ((f.filename, f.compress_size/f.file_size) for f in filelist
         if f.file_size != 0)
    print(min(t, key=lambda x: x[1])[0].split("/")[-1])
"""
