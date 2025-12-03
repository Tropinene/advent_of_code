import re
from functools import reduce
import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def find_lcm_of_list(numbers):
    return reduce(lcm, numbers)


def getData(file):
    with open(file, 'r') as f:
        data = f.readlines()
        f.close()
    return data


def genMap(data):
    dic = {}
    for line in data:
        line = line.strip()
        matches = re.findall(r'[A-Z]+', line)
        dic[matches[0]] = [matches[1], matches[2]]
    return dic


if __name__ == '__main__':
    file_path = './input.txt'
    lines = getData(file_path)

    instro = lines[0].strip()
    lines = lines[2:]
    network = genMap(lines)

    current = network.get('AAA')
    cnt = 0
    nextNode = 'AAA'
    while nextNode != 'ZZZ':
        for i in instro:
            if i == 'L':
                nextNode = current[0]
            elif i == 'R':
                nextNode = current[1]
            cnt += 1
            if nextNode == 'ZZZ':
                break
            current = network.get(nextNode)
    print(f'[Part1] : {cnt}')

    starts = []
    res = []
    for item in network.keys():
        if item[2] == 'A':
            starts.append(item)
    for start in starts:
        nextNode = start
        cnt = 0
        current = network.get(start)
        while nextNode[2] != 'Z':
            for i in instro:
                if i == 'L':
                    nextNode = current[0]
                elif i == 'R':
                    nextNode = current[1]
                cnt += 1
                if nextNode[2] == 'Z':
                    break
                current = network.get(nextNode)
        res.append(cnt)
    print(f'[Part2] : {find_lcm_of_list(res)}')
