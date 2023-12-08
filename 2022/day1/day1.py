file_path = './input.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()
    f.close()

lst = []
n = 0
for line in lines:
    line = line.strip('\n')
    if not line:
        lst.append(n)
        n = 0
        continue
    n += int(line)

lst.sort()
print(f'[Part 1] : {lst[-1]}')
print(f'[Part 2] : {lst[-1]+lst[-2]+lst[-3]}')
