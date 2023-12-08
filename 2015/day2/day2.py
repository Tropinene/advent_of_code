def getData(path):
    with open(path, 'r') as f:
        line = f.readlines()
        f.close
    return line


def calculate(l, w, h):
    small = min(l*w, l*h, w*h)
    return  2 * (l*w + l*h + w*h) + small


def calRibbon(l, w, h):
    big = max(l, w, h)
    return 2 * (l+w+h-big) + l*w*h


if __name__ == '__main__':
    file_path = './input.txt'
    lines = getData(file_path)

    res = 0
    ribbon = 0
    for line in lines:
        l, w, h = line.split('x')
        res += calculate(int(l), int(w), int(h))
        ribbon += calRibbon(int(l), int(w), int(h))

    print(f'[Part 1] : {res}')
    print(f'[Part 2] : {ribbon}')