def dive(lines: list[str], is_part2: bool) -> int:
    depth, hor_position = 0, 0
    aim = 0
    for line in lines:
        op, num = line.split()
        num = int(num)
        if op == "forward":
            if is_part2:
                depth += aim * num
            hor_position += num
        elif op == "down":
            if is_part2:
                aim += num
            else:
                depth += num
        elif op == 'up':
            if is_part2:
                aim -= num
            else:
                depth -= num

    return depth*hor_position


def main():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]

    print(f"[Part1] : {dive(lines, False)}")
    print(f"[Part2] : {dive(lines, True)}")


if __name__ == '__main__':
    main()
