import re


def getData(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def pprint(x, clock):
    if x <= clock % 40 <= x+2:
        print('█', end='')
    else:
        print(' ', end='')
    if clock % 40 == 0:
        print()


if __name__ == '__main__':
    file_path = './input.txt'
    data = getData(file_path)

    flag = False
    clock, x, p1 = 0, 1, 0
    print('[Part2]')
    for line in data:
        clock += 1
        pprint(x, clock)
        if (clock - 20) % 40 == 0:
            p1 += x * clock
        if line.startswith('addx'):
            clock += 1
            pprint(x, clock)
            if (clock - 20) % 40 == 0:
                p1 += x * clock
            x += int(re.findall(r'-?\d+', line)[0])
    print(f'[Part1] : {p1}')
