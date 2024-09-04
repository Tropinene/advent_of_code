def cal_area(instructions: list) -> int:
    area, x, y, c = 0, 0, 0, 0
    for direction, steps, _ in instructions:
        if direction == 'R':
            x += int(steps)
            area += y * int(steps)
        elif direction == 'L':
            x -= int(steps)
            area -= y * int(steps)
        elif direction == 'D':
            y += int(steps)
        elif direction == 'U':
            y -= int(steps)
        c += int(steps)

    return abs(area) + c // 2 + 1


def main():
    instructions = [line.strip().split() for line in open('input.txt', 'r').readlines()]
    p1 = cal_area(instructions)
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()