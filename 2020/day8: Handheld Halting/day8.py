import copy


def stop_before_second_exe(instructions: list[str]) -> int:
    acc = 0
    visited_idx, idx = [], 0
    while True:
        if idx in visited_idx:
            break
        visited_idx.append(idx)
        op, num = instructions[idx].split()
        if op == 'acc':
            acc += int(num)
        elif op == 'jmp':
            idx += int(num)
            continue
        idx += 1
    return acc


def check_terminate(instructions: list[str]) -> (int, bool):
    acc = 0
    visited_idx, idx = [], 0
    while True:
        if idx >= len(instructions):
            break
        if idx in visited_idx:
            return -1, False
        visited_idx.append(idx)
        op, num = instructions[idx].split()
        if op == 'acc':
            acc += int(num)
        elif op == 'jmp':
            idx += int(num)
            continue
        idx += 1
    return acc, True


def find_terminate(instructions: list[str]) -> int:
    for i in range(len(instructions)):
        backup = copy.deepcopy(instructions)
        if backup[i].startswith("nop"):
            backup[i] = backup[i].replace("nop", "jmp")
        elif backup[i].startswith("jmp"):
            backup[i] = backup[i].replace("jmp", "nop")

        acc, is_terminate = check_terminate(backup)
        if is_terminate:
            return acc


def main():
    instros = [x.strip() for x in open('input.txt', 'r').readlines()]

    p1 = stop_before_second_exe(instros)
    print(f"[Part1] : {p1}")

    p2 = find_terminate(instros)
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
