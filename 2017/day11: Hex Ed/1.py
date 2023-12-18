f = open("input.txt").read().strip().split(",")

x = 0
y = 0
dmax = 0


def dist(x, y):
    return (abs(x) + abs(y) + abs(x + y)) // 2


for d in f:
    if d == "n":
        y += 1
    elif d == "s":
        y -= 1
    elif d == "nw":
        x -= 1
        y += 1
    elif d == "ne":
        x += 1
    elif d == "sw":
        x -= 1
    elif d == "se":
        x += 1
        y -= 1

    dmax = max(dmax, dist(x, y))

print(dist(x, y))
print(dmax)