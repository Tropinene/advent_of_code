import math
from itertools import combinations, chain

boss = [103, 9, 2]
me = [100, 0, 0]

weapons = [
    [8, 4, 0],
    [10, 5, 0],
    [25, 6, 0],
    [40, 7, 0],
    [74, 8, 0]
]
armors = [
    [13, 0, 1],
    [31, 0, 2],
    [53, 0, 3],
    [75, 0, 4],
    [102, 0, 5]
]
rings = [
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3]
]


def choices():
    for w in combinations(weapons, 1):
        for a in chain(combinations(armors, 0), combinations(armors, 1)):
            for r in chain(combinations(rings, 0), combinations(rings, 1), combinations(rings, 2)):
                yield [w[0][i] + sum(armor[i] for armor in a) + sum(ring[i] for ring in r) for i in range(3)]


def win():
    if boss[1] <= me[2]:
        attcks1 = me[0]
    else:
        attcks1 = math.ceil(me[0] / (boss[1] - me[2]))
    if boss[2] >= me[1]:
        attcks2 = boss[0]
    else:
        attcks2 = math.ceil(boss[0] / (me[1] - boss[2]))

    if attcks2 <= attcks1:
        return True
    return False


if __name__ == '__main__':
    cheap = 999
    exp = -1
    for choice in choices():
        cost, damage, armor = choice
        me[1], me[2] = damage, armor
        if win() and cost < cheap:
            cheap = cost
        if not win() and cost > exp:
            exp = cost
    print(f'[Part1] : {cheap}')
    print(f'[Part2] : {exp}')
