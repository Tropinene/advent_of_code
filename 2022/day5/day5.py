# [G]                 [D] [R]
# [W]         [V]     [C] [T] [M]
# [L]         [P] [Z] [Q] [F] [V]
# [J]         [S] [D] [J] [M] [T] [V]
# [B]     [M] [H] [L] [Z] [J] [B] [S]
# [R] [C] [T] [C] [T] [R] [D] [R] [D]
# [T] [W] [Z] [T] [P] [B] [B] [H] [P]
# [D] [S] [R] [D] [G] [F] [S] [L] [Q]
#  1   2   3   4   5   6   7   8   9
# In this case, you should input the stack by yourself
# the operation can be read from .txt
import re
from copy import deepcopy

from matplotlib.cbook import Stack

file_path = './input.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()
    f.close()

cargo = [
    ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
    ['S', 'W', 'C'],
    ['R', 'Z', 'T', 'M'],
    ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
    ['G', 'P', 'T', 'L', 'D', 'Z'],
    ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
    ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
    ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
    ['Q', 'P', 'D', 'S', 'V']
]
lst = []
l = len(cargo)

for i in range(l):
    s = []
    for item in cargo[i]:
        s.append(item)
    lst.append(s)

lst1 = deepcopy(lst)
for line in lines:
    matches = re.findall(r'\d+', line)
    for i in range(int(matches[0])):
        tmp = lst[int(matches[1])-1].pop()
        lst[int(matches[2]) - 1].append(tmp)

p1 = ''
for i in range(l):
    p1 += lst[i][-1]

print(f'[Part1] : {p1}')

for line in lines:
    matches = re.findall(r'\d+', line)
    tmp = lst1[int(matches[1])-1][-int(matches[0]):]
    lst1[int(matches[1]) - 1] = lst1[int(matches[1])-1][:-int(matches[0])]
    lst1[int(matches[2]) - 1] += tmp
p2 = ''
for i in range(l):
    p2 += lst1[i][-1]

print(f'[Part2] : {p2}')
