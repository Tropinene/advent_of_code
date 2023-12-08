file_path = './input.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()
    f.close()

score = {'X': 1, 'Y': 2, 'Z': 3}
win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}

score2 = {'X': 0, 'Y': 3, 'Z': 6}
re_win = {'A': 2, 'B': 3, 'C': 1}
re_draw = {'A': 1, 'B': 2, 'C': 3}
re_lose = {'A': 3, 'B': 1, 'C': 2}

p1, p2 = 0, 0
for line in lines:
    a, b = line.strip('\n').split()
    p1 += score.get(b)
    if a == win.get(b):
        p1 += 6
    elif a == draw.get(b):
        p1 += 3

    p2 += score2.get(b)
    if b == 'X':
        p2 += re_lose.get(a)
    elif b == 'Y':
        p2 += re_draw.get(a)
    elif b == 'Z':
        p2 += re_win.get(a)

print(f'[Part 1] : {p1}')
print(f'[Part 2] : {p2}')

