from collections import defaultdict


def getData(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def count(win_lst, my_lst):
    res = 0
    for num in my_lst:
        if num in win_lst:
            res += 1
    return res


if __name__ == '__main__':
    file_path = 'input.txt'
    data = getData(file_path)

    point = 0
    copy = defaultdict(int)
    for i, line in enumerate(data):
        copy[i] += 1
        line = line.split(': ')[1].strip()
        line = line.replace('  ', ' ')
        lsts = line.split(' | ')
        win_nums = lsts[0].split(' ')
        my_nums = lsts[1].split(' ')
        n = count(win_nums, my_nums)
        if n:
            point += 2 ** (n-1)
        for j in range(n):
            copy[i+1+j] += copy[i]
    print(f'[Part 1] {int(point)}')
    print(f'[Part 2] {sum(copy.values())}')
