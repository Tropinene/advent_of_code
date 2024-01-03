def fuel(n):
    return n // 3 - 2


if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()

    p1, p2 = 0, 0
    for line in data:
        line = int(line.strip())
        f = fuel(line)
        p1 += f
        p2 += f
        while True:
            f = fuel(f)
            if f > 0:
                p2 += f
            else:
                break
    print(f"[Part1] : {p1}")
    print(f"[Part2] : {p2}")
