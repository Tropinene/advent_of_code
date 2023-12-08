file_path = './input.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()
    f.close()

c_side = len(lines[0].strip('\n'))
r_side = len(lines)
p1 = 0
for i in range(r_side):
    for j in range(c_side):
        if i == 0 or j == 0 or i == r_side - 1 or j == c_side - 1:
            p1 += 1
            continue
        if i > 0:
            flag = False
            for idx in range(i):
                if lines[idx][j] > lines[i][j]:
                    flag = True
                    break
                if flag:
                    continue
        if i < r_side - 1:
            flag = False
            for idx in range(i, r_side):
                if lines[idx][j] > lines[i][j]:
                    flag = True
                    break
                if flag:
                    continue
        if j > 0:
            flag = False
            for idx in range(j):
                if lines[i][idx] > lines[i][j]:
                    flag = True
                    break
                if flag:
                    continue
        if j < c_side - 1:
            flag = False
            for idx in range(j, c_side):
                if lines[i][idx] > lines[i][j]:
                    flag = True
                    break
                if flag:
                    continue
        print(f'i={i}, j={j}, num is {lines[i][j]}')
        p1 += 1
print(f'[Part1] : {p1}')
