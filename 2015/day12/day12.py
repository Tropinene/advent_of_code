import re
import json


def get_sum(d):
    if isinstance(d, int):
        return d
    elif isinstance(d, str):
        return 0
    elif isinstance(d, list):
        return sum(get_sum(x) for x in d)
    else:
        return 0 if any(x == 'red' for x in d.values()) else sum(get_sum(x) for x in d.values())


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        line = f.readline().strip()
        f.close()
    matches = re.findall(r'-?\d+', line)
    cnt = 0
    for num in matches:
        if num[0] == '-':
            cnt -= int(num[1:])
        else:
            cnt += int(num)
    print(f'[Part1] : {cnt}')

    d = json.loads(line)
    print(f'[Part2] : {get_sum(d)}')
