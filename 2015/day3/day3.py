def getData(path):
    with open(path, 'r') as f:
        line = f.readline()
        f.close
    return line

def part1(line):
    checked = [(0,0)]
    row = 0
    col = 0
    cnt = 1
    for i in line:
        if i == '>':
            col += 1
        elif i == '<':
            col -= 1
        elif i == '^':
            row += 1
        elif i == 'v':
            row -= 1
        
        if (row, col) not in checked:
            cnt += 1
            checked.append((row, col))
    return cnt

def part2(line):
    checked = [(0,0)]
    r1 = 0
    r2 = 0
    c1 = 0
    c2 = 0
    cnt = 1
    for idx, i in enumerate(line):
        if i == '>':
            if idx % 2 == 0:
                c1 += 1
            else:
                c2 += 1
        elif i == '<':
            if idx % 2 == 0:
                c1 -= 1
            else:
                c2 -= 1
        elif i == '^':
            if idx % 2 == 0:
                r1 += 1
            else:
                r2 += 1
        elif i == 'v':
            if idx % 2 == 0:
                r1 -= 1
            else:
                r2 -= 1
        
        if idx % 2 == 0:
            if (r1, c1) not in checked:
                cnt += 1
                checked.append((r1, c1))
        else:
            if (r2, c2) not in checked:
                cnt += 1
                checked.append((r2, c2))
    return cnt

if __name__ == '__main__':
    file_path = './input.txt'
    line = getData(file_path)
    
    res1 = part1(line)
    res2 = part2(line)
            
    print(f'[Part 1] : {res1}')
    print(f'[Part 2] : {res2}')