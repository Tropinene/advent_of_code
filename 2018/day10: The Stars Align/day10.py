import re


def parse_file() -> list:
    lines = open('input.txt', 'r').readlines()
    res = []

    for line in lines:
        matches = re.findall(r"-?\d+", line)
        matches = [int(item) for item in matches]
        res.append(matches)
    return res


def count_waiting_time(points: list) -> int:
    time = 0
    min_x, min_y = 102796, 102749
    while True:
        xs, ys = [], []
        for x, y, dx, dy in points:
            xs.append(x + dx * time)
            ys.append(y + dy * time)
        if max(xs) - min(xs) > min_x and max(ys) - min(ys) > min_y:
            return time - 1

        min_x = max(xs) - min(xs)
        min_y = max(ys) - min(ys)
        time += 1


def draw(points: list, time: int):
    xs, ys = [], []
    for x, y, dx, dy in points:
        xs.append(x+dx*time)
        ys.append(y+dy*time)

    for y in range(min(ys), max(ys)+1):
        for x in range(min(xs), max(xs)+1):
            if (x, y) in zip(xs, ys):
                print("█", end='')
            else:
                print(' ', end='')
        print()


def main():
    points = parse_file()
    p2 = count_waiting_time(points)
    print("[Part1]")
    draw(points, p2)
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
