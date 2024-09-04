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


def convert_RGB(instructions: list) -> list:
    new_instructions = []
    for _, _, ins in instructions:
        distance = int(ins[2:7], 16)
        direction = ins[-2]
        if direction == '0':
            new_instructions.append(['R', distance, ins])
        elif direction == '1':
            new_instructions.append(['D', distance, ins])
        elif direction == '2':
            new_instructions.append(['L', distance, ins])
        elif direction == '3':
            new_instructions.append(['U', distance, ins])

    return new_instructions


def main():
    instructions = [line.strip().split() for line in open('input.txt', 'r').readlines()]

    p1 = cal_area(instructions)
    print(f"[Part1] : {p1}")

    p2 = cal_area(convert_RGB(instructions))
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()