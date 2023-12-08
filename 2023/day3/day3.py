import re


def getData(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def check(row, span, matrix):
    symbol = ['*', '+', '#', '$', '@', '%', '&', '/', '-', '=']
    if row > 0:
        for i in range(span[0], span[1]):
            if matrix[row - 1][i] in symbol:
                return True
        if span[0] > 0 and matrix[row - 1][span[0] - 1] in symbol:
            return True
        if span[1] < len(matrix[row]) and matrix[row - 1][span[1]] in symbol:
            return True
    if row < len(matrix) - 1:
        for i in range(span[0], span[1]):
            if matrix[row + 1][i] in symbol:
                return True
        if span[0] > 0 and matrix[row + 1][span[0] - 1] in symbol:
            return True
        if span[1] < len(matrix[row]) and matrix[row + 1][span[1]] in symbol:
            return True
    if span[0] > 0:
        if matrix[row][span[0] - 1] in symbol:
            return True
    if span[1] < len(matrix[row]):
        if matrix[row][span[1]] in symbol:
            return True

    return False


if __name__ == '__main__':
    file_path = 'input.txt'
    matrix = getData(file_path)

    res = 0
    lst = []
    for i in range(len(matrix)):
        line = matrix[i]
        nums = re.findall(r'\d+', line)
        for num in nums:
            span = re.search(num, line).span()
            if check(i, span, matrix):
                res += int(num)
            else:
                lst.append(int(num))
    with open('2.txt', 'w') as f:
        lst.sort()
        f.write(str(lst))
        f.close()
    print(res)


