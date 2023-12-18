def dist(x, y):
    return (abs(x) + abs(y) + abs(x + y)) // 2


if __name__ == '__main__':
    data = open('input.txt', 'r').readline().strip().split(',')

    x, y, farthest = 0, 0, -1

    for i in data:
        if i == "n":
            y += 1
        elif i == "s":
            y -= 1
        elif i == "nw":
            x -= 1
            y += 1
        elif i == "ne":
            x += 1
        elif i == "sw":
            x -= 1
        elif i == "se":
            x += 1
            y -= 1
        farthest = max(farthest, dist(x, y))

    print(f"[Part1] : {dist(x, y)}")
    print(f"[Part2] : {farthest}")
