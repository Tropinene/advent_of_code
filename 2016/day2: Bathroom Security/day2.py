# give you a number map and follow the instructions
# if reach the edge of the map or the instruction end, stop and get the number you are
# part1: a rectangle map
# part2: a special map

import re


def getData(path):
    return open(path, 'r').readlines()


if __name__ == '__main__':
    file_path = './input.txt'
    lines = getData(file_path)
    res = []
    for line in lines:
        matches = re.findall(r'(L+|R+|U+|D+)', line.strip())
        loc = [1, 1]
        for i in matches:
            l = len(i)
            if i[0] == 'L':
                loc[1] = max(loc[1] - l, 0)
            elif i[0] == 'R':
                loc[1] = min(loc[1] + l, 2)
            elif i[0] == 'U':
                loc[0] = max(loc[0] - l, 0)
            elif i[0] == 'D':
                loc[0] = min(loc[0] + l, 2)
        res.append(str(loc[0] * 3 + loc[1] + 1))
    p1 = ''.join(res)
    print(f'[Part1] : {p1}')

    m = [
        ['#', '#', '1', '#', '#'],
        ['#', '2', '3', '4', '#'],
        ['5', '6', '7', '8', '9'],
        ['#', 'A', 'B', 'C', '#'],
        ['#', '#', 'D', '#', '#'],
    ]
    valid = [(0, 2), (1, 1), (1, 2), (1, 3), (2, 0),
             (2, 1), (2, 2), (2, 3), (2, 4), (3, 1),
             (3, 2), (3, 3), (4, 2)
             ]
    res = []
    for line in lines:
        loc = [2, 0]
        line = line.strip()
        for i in line:
            if i == 'L':
                next_loc = (loc[0], loc[1]-1)
                if next_loc in valid:
                    loc = list(next_loc)
            elif i == 'R':
                next_loc = (loc[0], loc[1]+1)
                if next_loc in valid:
                    loc = list(next_loc)
            elif i == 'U':
                next_loc = (loc[0]-1, loc[1])
                if next_loc in valid:
                    loc = list(next_loc)
            elif i == 'D':
                next_loc = (loc[0]+1, loc[1])
                if next_loc in valid:
                    loc = list(next_loc)
        res.append(m[loc[0]][loc[1]])
    p2 = ''.join(res)
    print(f'[Part2] : {p2}')
