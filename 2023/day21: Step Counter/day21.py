def create_directions(pos: tuple) -> list:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = []
    x, y = pos
    for dx, dy in dirs:
        res.append((x+dx, y+dy))
    return res


def step(start_points: list) -> list:
    next_points = []
    for x, y in start_points:
        next_steps = create_directions((x, y))
        for nx, ny in next_steps:
            if garden[nx][ny] != '#' and (nx, ny) not in next_points:
                next_points.append((nx, ny))
    return next_points


def find_S() -> tuple:
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if garden[i][j] == 'S':
                return i, j


def main():
    start = find_S()
    reach_plots = [start]
    for _ in range(64):
        reach_plots = step(reach_plots)
    print(f"[Part1] : {len(reach_plots)}")


if __name__ == '__main__':
    garden = [list(x.strip()) for x in open('input.txt', 'r').readlines()]
    main()
