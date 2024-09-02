def is_wall(x: int, y: int, luckyNum: int) -> bool:
    n = x * x + 3 * x + 2 * x * y + y + y * y + luckyNum
    bin_n = bin(n)[2:]
    num_1 = bin_n.count('1')
    if num_1 % 2 == 0:
        return False
    return True


def move(pos: tuple, direction: tuple, luckyNum: int) -> list:
    new_x = pos[1][0] + direction[0]
    new_y = pos[1][1] + direction[1]
    distance = pos[0] + 1
    if new_x >= 0 and new_y >= 0 and is_wall(new_x, new_y, luckyNum) is False:
        return [(distance, (new_x, new_y))]
    return []


def solve(luckyNum: int, start: tuple, destination: tuple) -> int:
    visited, check = set(), []
    curPosition = (0, start)
    visited.add(curPosition)
    check.append(curPosition)

    while len(check) > 0:
        curPosition = check.pop(0)
        if curPosition[1] == destination:
            return curPosition[0]
        nextPositions = move(curPosition, (1, 0), luckyNum) \
                        + move(curPosition, (-1, 0), luckyNum) \
                        + move(curPosition, (0, 1), luckyNum) \
                        + move(curPosition, (0, -1), luckyNum)
        for nextPosition in nextPositions:
            if nextPosition[1] not in visited:
                check.append(nextPosition)
                visited.add(nextPosition[1])


def solve2(luckyNum: int, start: tuple, maxSteps: int) -> int:
    visited, check = set(), []
    curPosition = (0, start)
    visited.add(curPosition[1])
    check.append(curPosition)

    while len(check) > 0:
        curPosition = check.pop(0)
        if curPosition[0] == maxSteps:
            return len(visited)
        nextPositions = move(curPosition, (1, 0), luckyNum) \
                        + move(curPosition, (-1, 0), luckyNum) \
                        + move(curPosition, (0, 1), luckyNum) \
                        + move(curPosition, (0, -1), luckyNum)
        for nextPosition in nextPositions:
            if nextPosition[1] not in visited:
                check.append(nextPosition)
                visited.add(nextPosition[1])


def main():
    p1 = solve(1364, (1, 1), (31, 39))
    print(f"[Part1] : {p1}")

    p2 = solve2(1364, (1, 1), 50)
    print(f"[Part2] : {p2}")

    return


if __name__ == '__main__':
    main()
