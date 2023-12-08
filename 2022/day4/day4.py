import re

file_path = './input.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()
    f.close()

p1, p2 = 0, 0
for line in lines:
    a, b = line.strip('\n').split(',')
    ma = re.findall(r'\d+', a)
    mb = re.findall(r'\d+', b)
    set1 = set(range(int(ma[0]), int(ma[1])+1))
    set2 = set(range(int(mb[0]), int(mb[1])+1))
    if set1.issubset(set2) or set2.issubset(set1):
        p1 += 1
    if set1 & set2:
        p2 += 1

print(f'[Part 1] : {p1}')
print(f'[Part 2] : {p2}')
