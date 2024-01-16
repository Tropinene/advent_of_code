from collections import Counter, defaultdict
import math


def reduce(x, y):
    divisor = math.gcd(x, y)
    return x // divisor, y // divisor


def detect(d):
    asteroids = [(x, y) for y, row in enumerate(d) for x, c in enumerate(row) if c == '#']

    best = (0, 0, 0)

    for i, (ax, ay) in enumerate(asteroids):
        angles = defaultdict(list)
        for j, (ox, oy) in enumerate(asteroids):
            if i == j:
                continue

            xdiff, ydiff = reduce(ox - ax, oy - ay)
            if xdiff == 0:
                ydiff = 1 if ydiff > 0 else -1

            angles[(xdiff, ydiff)].append((ox, oy))

        score = len(angles)
        best = max(best, (score, ax, ay))

    return best[0]


if __name__ == '__main__':
    lines = open("input.txt", "r").readlines()
    lines = [x.strip() for x in lines]

    p1 = detect(lines)
    print(f"[Part1] {p1}")
    # todo part2
