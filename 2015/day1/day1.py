def getData(path):
    with open(path, 'r') as f:
        line = f.readline()
        f.close
    return line


if __name__ == '__main__':
    file_path = './input.txt'
    line = getData(file_path)

    cnt = 0
    basement = 0
    for idx, i in enumerate(line):
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if not basement and cnt == -1:
            basement = idx + 1

    print(f'[Part 1] : {cnt}')
    print(f'[Part 2] : {basement}')