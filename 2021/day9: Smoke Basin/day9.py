def get_adjacent(pos: tuple, limit: tuple) -> list:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    res = []
    for d in directions:
        new_x = pos[0] + d[0]
        new_y = pos[1] + d[1]
        if 0 <= new_x < limit[0] and 0 <= new_y < limit[1]:
            res.append((new_x, new_y))
    return res


def main():
    lines = [list(x.strip()) for x in open('input.txt', 'r').readlines()]

    limit = (len(lines), len(lines[0]))
    p1 = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            adjacents = get_adjacent((i, j), limit)
            if all(lines[i][j] < lines[pos[0]][pos[1]] for pos in adjacents):
                p1 += int(lines[i][j]) + 1
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()