import copy


def solve(jumps, is_part2):
    step, idx = 0, 0
    while idx < len(jumps):
        jump = jumps[idx]
        if is_part2:
            if jumps[idx] >= 3:
                jumps[idx] -= 1
            else:
                jumps[idx] += 1
        else:
            jumps[idx] += 1
        idx += jump
        step += 1

    return step


if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    data = [int(x.strip()) for x in data]

    p1 = solve(copy.deepcopy(data), False)
    print(f"[Part1] : {p1}")

    p2 = solve(copy.deepcopy(data), True)
    print(f"[Part2] : {p2}")
