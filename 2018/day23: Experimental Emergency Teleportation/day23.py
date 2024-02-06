import re


def parse_file() -> (list, tuple):
    lines = open('input.txt', 'r').readlines()
    max_r = -1
    nanobots, max_one = [], None
    for line in lines:
        matches = re.findall(r'-?\d+', line)
        nanobot = tuple(int(item) for item in matches)
        if nanobot[3] > max_r:
            max_one, max_r = nanobot, max(nanobot[3], max_r)
        nanobots.append(nanobot)
    return nanobots, max_one


def count_distance(a: tuple, b: tuple) -> int:
    res = 0
    for i in range(3):
        res += abs(a[i] - b[i])
    return res


def check(bots: list, cur: tuple) -> int:
    r, res = cur[3], 0
    for bot in bots:
        if count_distance(bot[:3], cur[:3]) <= r:
            res += 1
    return res


def main():
    nanobots, target = parse_file()
    p1 = check(nanobots, target)
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()
