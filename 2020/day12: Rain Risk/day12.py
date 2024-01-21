import math


def cal_distance(actions: list[str]) -> int:
    directions = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1)}
    dir_list = ['E', 'S', 'W', 'N']
    pos = (0, 0)

    direction = 'E'

    for action in actions:
        step = int(action[1:])
        op = action[0]

        if op == 'F':
            dx, dy = directions[direction]
        elif op in directions:
            dx, dy = directions[op]
        elif op == 'R':
            idx = (dir_list.index(direction) + step // 90) % 4
            direction = dir_list[idx]
            continue
        elif op == 'L':
            idx = (dir_list.index(direction) - step // 90) % 4
            direction = dir_list[idx]
            continue

        pos = (pos[0] + step * dx, pos[1] + step * dy)

    return abs(pos[0]) + abs(pos[1])


def cal_distance2(actions: list[str]) -> int:
    pos, waypoint_pos = (0, 0), (10, 1)

    for action in actions:
        op, value = action[0], int(action[1:])

        if op == 'F':
            pos = (pos[0] + value * waypoint_pos[0], pos[1] + value * waypoint_pos[1])
        elif op in ('N', 'S', 'E', 'W'):
            dx, dy = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}[op]
            waypoint_pos = (waypoint_pos[0] + value * dx, waypoint_pos[1] + value * dy)
        elif op in ('R', 'L'):
            angle = value if op == 'R' else -value
            angle_rad = math.radians(angle)
            new_x = round(waypoint_pos[0] * math.cos(angle_rad) + waypoint_pos[1] * math.sin(angle_rad))
            new_y = round(-waypoint_pos[0] * math.sin(angle_rad) + waypoint_pos[1] * math.cos(angle_rad))
            waypoint_pos = (new_x, new_y)

    return abs(pos[0]) + abs(pos[1])


def main():
    actions = [x.strip() for x in open('input.txt', 'r').readlines()]
    print(f"[Part1] : {cal_distance(actions)}")
    print(f"[Part2] : {cal_distance2(actions)}")


if __name__ == '__main__':
    main()
