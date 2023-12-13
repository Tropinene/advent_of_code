def rays(grid, y, x):
    return [
        [grid[y][dx] for dx in range(x-1, -1, -1)],
        [grid[y][dx] for dx in range(x + 1, len(grid[0]))],
        [grid[dy][x] for dy in range(y-1, -1, -1)],
        [grid[dy][x] for dy in range(y + 1, len(grid))],
    ]


def part1(lines):
    height, width = len(lines), len(lines[0])
    num_visible = 0

    for i in range(height):
        for j in range(width):
            is_visible = False
            for ray in rays(lines, i, j):
                if ray == []:
                    is_visible = True
                    break
                flag = True
                for tree in ray:
                    if not tree < lines[i][j]:
                        flag = False
                        break
                if flag:
                    is_visible = True
                    break
            if is_visible:
                num_visible += 1

    return num_visible


def part2(lines):
    height, width = len(lines), len(lines[0])
    max_score = -1

    for i in range(height):
        for j in range(width):
            res = 1
            for ray in rays(lines, i, j):
                cnt = 0
                for tree in ray:
                    cnt += 1
                    if tree >= lines[i][j]:
                        break
                res *= cnt
            max_score = max(max_score, res)

    return max_score


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        for line in f.readlines():
            lines.append(list(map(int, list(line.rstrip()))))

    print(f'[Part1] : {part1(lines)}')
    print(f'[Part2] : {part2(lines)}')
