import itertools


def getData(path):
    with open(path, 'r') as f:
        data = f.readlines()
        f.close()
    return data


def permute_containers(containers, litres):
    total = 0
    for i, b in enumerate(containers):
        if b > litres:
            continue
        elif b == litres:
            total += 1
        else:
            total += permute_containers(containers[i + 1:], litres - b)
    return total


def permute_containers2(containers, litres, level):
    if level == 0:
        return 0
    total = 0
    for i, b in enumerate(containers):
        if b > litres:
            continue
        elif b == litres:
            total += 1
        else:
            total += permute_containers2(containers[i + 1:], litres - b, level - 1)
    return total


if __name__ == '__main__':
    file_path = './input.txt'
    data = getData(file_path)

    containers = []
    for line in data:
        containers.append(int(line.strip()))

    containers.sort()
    print(containers)
    p1 = permute_containers(containers, 150)
    print(f'[Part1] : {p1}')

    for i in range(100):
        p2 = permute_containers2(containers, 150, i)
        if p2:
            print(f'[Part2] : {p2}')
            break
