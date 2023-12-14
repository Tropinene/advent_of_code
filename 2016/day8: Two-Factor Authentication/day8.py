# a pixels matrix with three kinds of instructions [rect | rotate row | rotate column]
# part1: count shining pixels
# part2: figure out the characters showed by matrix

import copy
import re


def print_eg(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for r in range(row):
        for c in range(col):
            if lights[r][c]:
                print('█', end="")
            else:
                print(' ', end="")
        print()
    print()


if __name__ == '__main__':
    lights = [[0] * 50 for _ in range(6)]
    instros = open("input.txt", "r").readlines()

    for instro in instros:
        if instro.startswith("rect"):
            matches = re.findall(r"\d+", instro)
            for i in range(int(matches[1])):
                for j in range(int(matches[0])):
                    lights[i][j] = 1
        elif instro.startswith("rotate row"):
            matches = re.findall(r"\d+", instro)
            offset = int(matches[1])
            tmp = copy.deepcopy(lights)
            for j in range(50):
                tmp[int(matches[0])][j] = lights[int(matches[0])][(j - offset + 50) % 50]
            lights = copy.deepcopy(tmp)
        else:
            matches = re.findall(r"\d+", instro)
            offset = int(matches[1])
            tmp = copy.deepcopy(lights)
            for i in range(6):
                tmp[i][int(matches[0])] = lights[(i - offset + 6) % 6][int(matches[0])]
            lights = copy.deepcopy(tmp)
    p1 = 0
    for line in lights:
        p1 += sum(line)
    print(f"[Part1] : {p1}")
    print('[Part2]')
    print_eg(lights)
