def parse() -> list:
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    rows, cols = len(data), len(data[0])

    res = []
    for r in range(rows):
        for j in range(cols):
            if data[r][j] == '#':
                res.append((r, j))
    return res


def move(elfs: list, direction: list) -> list:
    plan_to_move = {}
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for e in elfs:
        if all((e[0] + n[0], e[1] + n[1]) not in elfs for n in neighbors):
            plan_to_move[e] = e
            continue

        for d in direction:
            if all((e[0] + item[0], e[1] + item[1]) not in elfs for item in d):
                new_pos = (e[0] + d[1][0], e[1] + d[1][1])
                same_position = False
                for key, value in plan_to_move.items():
                    if new_pos == value:
                        plan_to_move[key] = key
                        plan_to_move[e] = e
                        same_position = True
                        break
                if not same_position:
                    plan_to_move[e] = new_pos
                break
        if e not in plan_to_move:
            plan_to_move[e] = e

    return list(plan_to_move.values())


def main():
    elfs = parse()
    d = [[(-1, -1), (-1, 0), (-1, 1)],
         [(1, -1), (1, 0), (1, 1)],
         [(-1, -1), (0, -1), (1, -1)],
         [(-1, 1), (0, 1), (1, 1)]]

    for _ in range(10):
        new_elfs = move(elfs, d)
        elfs = new_elfs
        d = d[1:] + d[:1]

    x_values = [x for x, y in elfs]
    y_values = [y for x, y in elfs]
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)

    p1 = (max_x - min_x + 1) * (max_y - min_y + 1) - len(elfs)
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()
