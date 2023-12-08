import re


def getData(path):
    with open(path, 'r') as f:
        data = f.readlines()
        f.close()
    return data


if __name__ == '__main__':
    file_path = './input.txt'
    lines = getData(file_path)

    lst = []
    for line in lines:
        matches = re.findall(r'\d+', line)
        matches = list(map(int, matches))
        lst.append(matches)
    res = []
    for item in lst:
        dis = item[0] * (2503 // (item[1]+item[2])) * item[1]
        remain = 2503 % (item[1]+item[2])
        if remain > item[1]:
            dis += item[0] * item[1]
        else:
            dis += item[0] * remain
        res.append(dis)

    res.sort()
    print(f'[Part1] : {res[-1]}')

    dis = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    score = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 2504):
        for idx, item in enumerate(lst):
            if i % (item[1] + item[2]) != 0:
                if i % (item[1] + item[2]) <= item[1]:
                    dis[idx] += item[0]
        max_value = max(dis)
        max_indices = [index for index, value in enumerate(dis) if value == max_value]
        for indice in max_indices:
            score[indice] += 1

    score.sort()
    print(f'[Part2] : {score[-1]}')