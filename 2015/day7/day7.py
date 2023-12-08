def getData(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def f(r, vals, index):
    if r in vals:
        return vals[r]
    l = index[r]
    w = l.split()
    if w[1] == '->':
        ret = int(w[0]) if w[0].isdigit() else f(w[0], vals, index)
    elif w[0] == 'NOT':
        ret = ~f(w[1], vals, index)
    elif w[1] == 'AND':
        v1 = int(w[0]) if w[0].isdigit() else f(w[0], vals, index)
        ret = v1 & f(w[2], vals, index)
    elif w[1] == 'OR':
        ret = f(w[0], vals, index) | f(w[2], vals, index)
    elif w[1] == 'RSHIFT':
        ret = f(w[0], vals, index) >> int(w[2])
    elif w[1] == 'LSHIFT':
        ret = f(w[0], vals, index) << int(w[2])
    vals[r] = ret
    return ret


def f2(r, vals, index):
    if r == 'b':
        return f('a', vals, index)
    f('b', vals, index)


if __name__ == "__main__":
    file_path = './input.txt'
    lines = getData(file_path)

    idx = {}
    for line in lines:
        line = line.strip()
        idx[line.split()[-1]] = line

    var = {}
    p1 = f('a', var, idx)
    print(f'[Part1] : {p1}')
    p2 = f2('a', var, idx)
    print(f'[Part2] : {p2}')
