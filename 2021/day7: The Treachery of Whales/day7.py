def count_fuel(hor_pos: int, positions: list, is_part2: bool) -> int:
    cnt = 0
    for i in positions:
        if is_part2:
            tmp = abs(i-hor_pos)
            cnt += (1+tmp) * tmp // 2
        else:
            cnt += abs(i-hor_pos)
    return cnt


def main():
    inp = open('input.txt', 'r').readline()
    positions = [int(x) for x in inp.split(',')]

    p1, p2 = float('inf'), float('inf')
    for i in range(min(positions), max(positions)+1):
        tmp = count_fuel(i, positions, False)
        tmp2 = count_fuel(i, positions, True)
        if tmp < p1:
            p1 = tmp
        if tmp2 < p2:
            p2 = tmp2
    print(f"[Part1] : {p1}")
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()