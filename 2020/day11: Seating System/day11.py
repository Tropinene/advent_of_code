import copy


def create_check_list(pos: tuple, limit: tuple) -> list[tuple]:
    d_x, d_y = [-1, 0, 1], [-1, 0, 1]

    res = []
    x_limit, y_limit = limit

    for dx in d_x:
        for dy in d_y:
            if dx == dy == 0:
                continue

            x, y = pos[0] + dx, pos[1] + dy
            if 0 <= x < x_limit and 0 <= y < y_limit:
                res.append((x, y))

    return res


def create_check_list2(pos: tuple, limit: tuple) -> list[list[tuple]]:
    res = []

    # 水平方向
    tmp = [(x, pos[1]) for x in range(pos[0] - 1, -1, -1)]
    res.append(tmp)
    tmp = [(x, pos[1]) for x in range(pos[0] + 1, limit[0])]
    res.append(tmp)

    # 垂直方向
    tmp = [(pos[0], y) for y in range(pos[1] - 1, -1, -1)]
    res.append(tmp)
    tmp = [(pos[0], y) for y in range(pos[1] + 1, limit[1])]
    res.append(tmp)

    # 对角线方向
    tmp = [(x, y) for x, y in zip(range(pos[0] + 1, limit[0]), range(pos[1] + 1, limit[1]))]
    res.append(tmp)
    tmp = [(x, y) for x, y in zip(range(pos[0] + 1, limit[0]), range(pos[1] - 1, -1, -1))]
    res.append(tmp)
    tmp = [(x, y) for x, y in zip(range(pos[0] - 1, -1, -1), range(pos[1] + 1, limit[1]))]
    res.append(tmp)
    tmp = [(x, y) for x, y in zip(range(pos[0] - 1, -1, -1), range(pos[1] - 1, -1, -1))]
    res.append(tmp)

    return res


def go_round(seats: list[list[str]], threshold: int) -> list[list[str]]:
    res = copy.deepcopy(seats)
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            occupied_cnt = 0
            adjacents = create_check_list((i, j), (len(seats), len(seats[0])))
            for (x, y) in adjacents:
                if seats[x][y] == '#':
                    occupied_cnt += 1
            if seats[i][j] == 'L' and occupied_cnt == 0:
                res[i][j] = '#'
            if seats[i][j] == '#' and occupied_cnt >= threshold:
                res[i][j] = 'L'
    return res


def go_round2(seats: list[list[str]], threshold: int) -> list[list[str]]:
    res = copy.deepcopy(seats)
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            occupied_cnt = 0
            adjacents = create_check_list2((i, j), (len(seats), len(seats[0])))
            for dir in adjacents:
                for (x, y) in dir:
                    if seats[x][y] == '#':
                        occupied_cnt += 1
                        break
                    if seats[x][y] == 'L':
                        break
            if seats[i][j] == 'L' and occupied_cnt == 0:
                res[i][j] = '#'
            if seats[i][j] == '#' and occupied_cnt >= threshold:
                res[i][j] = 'L'
    return res


def count_occupied(seats: list[list[str]]) -> int:
    occupied_count = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                occupied_count += 1
    return occupied_count


def main():
    seats = [list(x.strip()) for x in open('input.txt', 'r').readlines()]

    while True:
        tmp = go_round(seats, 4)
        if tmp == seats:
            break
        seats = tmp

    print(f"[Part1] : {count_occupied(seats)}")

    while True:
        tmp = go_round2(seats, 5)
        if tmp == seats:
            break
        seats = tmp

    print(f"[Part2] : {count_occupied(seats)}")


if __name__ == '__main__':
    main()
