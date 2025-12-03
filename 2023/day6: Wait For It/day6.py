import re


def getData(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def calc(time, dis):
    v = 0
    for v in range(time):
        if v * (time-v) > dis:
            return time - v*2 + 1
    #         cnt += 1
    # return cnt


if __name__ == '__main__':
    file_path = './input.txt'
    lines = getData(file_path)

    times = re.findall(r'\d+', lines[0])
    distance = re.findall(r'\d+', lines[1])

    p1 = 1
    for i in range(len(times)):
        p1 *= calc(int(times[i]), int(distance[i]))
    print(f'[Part1] : {p1}')

    p2 = calc(int(''.join(times)), int(''.join(distance)))
    print(f'[Part2] : {p2}')
