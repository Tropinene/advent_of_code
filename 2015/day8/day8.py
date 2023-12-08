def getData(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


if __name__ == '__main__':
    file_path = './input.txt'
    lines = getData(file_path)

    code, value = 0, 0
    p2 = 0
    for line in lines:
        line = line.strip()
        code += len(line)
        p2 = p2 + 4 + line[1:-1].count("\\") + line[1:-1].count("\"")

        line = line.replace('\\\\', 'a')
        tmp = line[1:-1].split('\\')
        lst = []
        if tmp[0]:
            lst.append(tmp[0])
        for item in tmp[1:]:
            if len(item) == 0:
                lst.append('\\')
            else:
                if item[0] == 'x':
                    lst.append(item[2:])
                else:
                    lst.append(item)
        line = ''.join(lst)
        value += len(line)
    print(f'[Part1] : {code - value}')
    print(f'[Part2] : {p2}')
