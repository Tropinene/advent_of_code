file_path = './input.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()
    f.close()

p1 = 0
for line in lines:
    line = line.strip('\n')
    mid = int(len(line) / 2)
    uni = set(line[:mid]) & set(line[mid:])

    n = list(uni)[0]
    if n.islower():
        p1 += ord(n) - ord('a') + 1
    else:
        p1 += ord(n) - ord('A') + 27

print(f'[Part 1] : {p1}')

p2 = 0
for i in range(0, len(lines), 3):
    uni = set(lines[i].strip('\n')) & set(lines[i+1].strip('\n')) & set(lines[i+2].strip('\n'))
    n = list(uni)[0]
    if n.islower():
        p2 += ord(n) - ord('a') + 1
    else:
        p2 += ord(n) - ord('A') + 27

print(f'[Part 2] : {p2}')
