# Falling time is 1 second, the disk spends 1 second to next position
# part1: figure out the first time to press the button
# part2: just add a new disk

import re


def get_press_time(disks):
    press_time = 0
    while True:
        current = press_time + 1
        is_get = True
        for disk in disks:
            position = (disk[1] + current) % disk[0]
            if position == 0:
                current += 1
            else:
                is_get = False
                break
        if is_get:
            break
        else:
            press_time += 1
    return press_time


if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    num_disks = len(data)

    disks_info = []
    for line in data:
        matches = re.findall(r'\d+', line)
        tmp = [int(matches[1]), int(matches[-1])]
        disks_info.append(tmp)

    print(f'[Part1] : {get_press_time(disks_info)}')
    disks_info.append([11, 0])
    print(f'[Part2] : {get_press_time(disks_info)}')
