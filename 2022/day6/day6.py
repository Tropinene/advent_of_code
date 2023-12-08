file_path = './input.txt'
with open(file_path, 'r') as f:
    line = f.readline()
    f.close()

lst = []
cnt = 14
i = 0
while i < len(line):
    if line[i] not in lst:
        lst.append(line[i])
        cnt -= 1
        if cnt == 0:
            print(f'[Part1] : {i+1}')
            break
        i += 1
    else:
        back = len(lst) - lst.index(line[i])
        i = i - back + 1
        lst.clear()
        cnt = 14
