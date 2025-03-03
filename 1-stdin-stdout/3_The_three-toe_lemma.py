'''
Лемма о трёх носках

Анри и Дима, имея на руках ящик с бесконечным количеством носков, решили сыграть в игру. 
Ребята по очереди достают из ящика произвольное количество носков, и после неопределенного 
числа ходов игра заканчивается. Если тот, кто сделал последний ход, вытащил четное количество носков — 
он побеждает, в противном случае проигрывает.

Напишите программу, которая определяет победителя в данной игре, если первый ход делает Анри.

Формат входных данных
На вход программе подается произвольное количество строк, в каждой строке записано натуральное число — 
количество носков, которые вытащил один из игроков.

Формат выходных данных
Программа должна определить победителя в игре, правила которой представлены в условии задачи, и вывести его имя.
'''
import sys

names = ['Анри', 'Дима']
name, numb = 0, 0
for n, line in enumerate(sys.stdin):
    numb = int(line.strip())
    name = n
if name % 2 == 0 and numb % 2 == 0 or name % 2 == 1 and numb % 2 == 1:
    print(names[0])
else:
    print(names[1])