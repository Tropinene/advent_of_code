import re
import copy


# def do_step(pos, vel):
#     num_bodies = len(pos)
#     rows = num_bodies
#     cols = len(pos[0])
#
#     for j in range(cols):
#         for i in range(rows):
#             # Count elements greater than pos[i][j]
#             gt = sum(1 for x in pos if x[j] > pos[i][j])
#             lt = sum(1 for x in pos if x[j] < pos[i][j])
#             vel[i][j] += gt - lt
#
#     for i in range(rows):
#         for j in range(cols):
#             pos[i][j] += vel[i][j]
#
#     return pos, vel
#
#
# if __name__ == '__main__':
#     bodys = open('input.txt', 'r').readlines()
#     pattern = re.compile(r'[+-]?\d+')
#
#     pos = []
#     for body in bodys:
#         values = pattern.findall(body)
#         values = [int(x) for x in values]
#         pos.append(values)
#     vel = [[0, 0, 0] for _ in range(4)]
#     pos2 = copy.deepcopy(pos)
#     for _ in range(1000):
#         pos, vel = do_step(pos, vel)
#
#     p1 = 0
#     for i in range(len(pos)):
#         pot = sum(abs(x) for x in pos[i])
#         kin = sum(abs(x) for x in vel[i])
#         p1 += pot * kin
#
#     print(f"[Part1] {p1}")
#
#     p2 = 1000
#     while pos != pos2:
#         p2 += 1
#         pos, vel = do_step(pos, vel)
#         if p2 % 100000 == 0:
#             print(p2)
#     print(f"[Part2] {p2}")

import re
import copy
import numpy as np
from numba import jit

@jit(nopython=True)
def do_step_numba(pos, vel):
    num_bodies, cols = pos.shape

    for j in range(cols):
        for i in range(num_bodies):
            gt = np.sum(pos[:, j] > pos[i, j])
            lt = np.sum(pos[:, j] < pos[i, j])
            vel[i, j] += gt - lt
    pos += vel

    return pos, vel


if __name__ == '__main__':
    bodys = open('input.txt', 'r').readlines()
    pattern = re.compile(r'[+-]?\d+')

    pos = []
    for body in bodys:
        values = pattern.findall(body)
        values = [int(x) for x in values]
        pos.append(values)
    pos = np.array(pos)
    vel = np.zeros_like(pos)
    pos2 = copy.deepcopy(pos)

    for _ in range(1000):
        pos, vel = do_step_numba(pos, vel)

    p1 = 0
    for i in range(len(pos)):
        pot = sum(abs(x) for x in pos[i])
        kin = sum(abs(x) for x in vel[i])
        p1 += pot * kin

    print(f"[Part1] {p1}")

    p2 = 1001
    pos, vel = do_step_numba(pos, vel)
    while not np.array_equal(pos, pos2):
        p2 += 1
        pos, vel = do_step_numba(pos, vel)
        if p2 % 10000000 == 0:
            print(p2)

    print(f"[Part2] {p2}")

