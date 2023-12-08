import re


def getData(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def check(s):
    matches = re.findall(r'a|e|i|o|u', s)
    if len(matches) < 3:
        return False
    matches = re.findall(r'(.)\1', s)
    if not matches:
        return False
    matches = re.findall(r'ab|cd|pq|xy', s)
    if matches:
        return False
    return True


def check2(s):
    flag = False
    for idx, i in enumerate(s):
        if idx+2 < len(s) and i == s[idx+2]:
            flag = True
    if not flag:
        return False
    flag = False
    for idx, i in enumerate(s):
        if idx+1 >= len(s):
            break
        tmp = i+s[idx+1]
        if s[idx+2:].find(tmp) != -1:
            flag = True
            break
    return flag


if __name__ == '__main__':
    lines = getData('./input.txt')
    p1, p2 = 0, 0
    for line in lines:
        line = line.strip()
        if check(line):
            p1 += 1
        if check2(line):
            p2 += 1
    print(f'[Part1] : {p1}')
    print(f'[Part2] : {p2}')
