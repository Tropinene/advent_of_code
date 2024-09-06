def find_position(heightmap: list, target: str) -> tuple:
    rows, cols = len(heightmap), len(heightmap[0])
    for row in range(rows):
        for col in range(cols):
            if heightmap[row][col] == target:
                return row, col


def find_start(heightmap: list) -> list:
    res = []
    rows, cols = len(heightmap), len(heightmap[0])
    for row in range(rows):
        for col in range(cols):
            if heightmap[row][col] == 'a':
                res.append((row, col))
    return res


def count_height(inp: str) -> int:
    if inp == 'S':
        return 0
    if inp == 'E':
        return 25
    return ord(inp) - ord('a')


def bfs(heightmap: list, s: tuple, e: tuple) -> int:
    visited, path = set(), [(s[0], s[1], 0)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited.add(s)

    while len(path) > 0:
        x, y, step = path.pop(0)
        if (x, y) == e:
            return step

        cur_height = count_height(heightmap[x][y])

        for dx, dy in directions:
            next_x, next_y = x+dx, y+dy
            if 0 <= next_x < len(heightmap) and 0 <= next_y < len(heightmap[0]) and (next_x, next_y) not in visited:
                next_height = count_height(heightmap[next_x][next_y])
                if next_height <= cur_height + 1:
                    visited.add((next_x, next_y))
                    path.append((next_x, next_y, step+1))

    return 10**9


def main():
    heightmap = [list(line.strip()) for line in open('input.txt', 'r').readlines()]
    start, end = find_position(heightmap, 'S'), find_position(heightmap, 'E')

    p1 = bfs(heightmap, start, end)
    print(f"[Part1] : {p1}")

    starts = find_start(heightmap)
    p2 = float('inf')
    for start in starts:
        p2 = min(p2, bfs(heightmap, start, end))
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
