def create_adjacents(cur, limit):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    res = []
    for dx, dy in directions:
        new_x, new_y = cur[0]+dx, cur[1]+dy
        if 0 <= new_x < limit[0] and 0 <= new_y < limit[1]:
            res.append((new_x, new_y))
    return res


def clean(datas):
    cnt = 0
    for i in range(len(datas)):
        for j in range(len(datas[0])):
            if datas[i][j] > 9:
                datas[i][j] = 0
                cnt += 1
    return datas, cnt


def step(octopus):
    shining_list = []
    height = len(octopus)
    width = len(octopus[0])

    for i in range(height):
        for j in range(width):
            octopus[i][j] += 1
            if octopus[i][j] > 9:
                shining_list.append((i, j))

    idx = 0
    while len(shining_list) > idx:
        x, y = shining_list[idx]
        adjacents = create_adjacents((x, y), (height, width))
        for i, j in adjacents:
            octopus[i][j] += 1
            if octopus[i][j] > 9 and (i, j) not in shining_list:
                shining_list.append((i, j))
        idx += 1
    return octopus


def main():
    octopus = [[int(x) for x in line.strip()] for line in open('input.txt', 'r').readlines()]

    p1, p2 = 0, 0
    while True:
        p2 += 1
        octopus = step(octopus)
        octopus, tmp = clean(octopus)
        p1 += tmp
        if p2 == 100:
            print(f"[Part1] : {p1}")
        if tmp == 100:
            print(f"[Part2] : {p2}")
            break


if __name__ == "__main__":
    main()
