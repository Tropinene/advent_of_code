import math


def is_prime(b):
    if b % 2 == 0 and b > 2:
        return False
    for d in range(3, int(math.sqrt(b)) + 1, 2):
        if b % d == 0:
            return False
    return True


def cpu(reg, instros, is_part2):
    mul_cnt = 0
    idx = 0
    while idx < len(instros):
        if idx == 8 and is_part2:
            if is_prime(reg['b']):
                reg['f'] = 1
            else:
                reg['f'] = 0
            idx = 24
        lst = instros[idx].split()
        if lst[2].isdigit() or lst[2].startswith('-'):
            val = int(lst[2])
        else:
            val = reg[lst[2]]

        if lst[0] == 'set':
            reg[lst[1]] = val
        elif lst[0] == 'sub':
            reg[lst[1]] -= val
        elif lst[0] == 'mul':
            mul_cnt += 1
            reg[lst[1]] *= val
        elif lst[0] == 'jnz':
            if lst[1].isdigit() or lst[1].startswith('-'):
                condition = int(lst[1])
            else:
                condition = reg[lst[1]]
            if condition != 0:
                idx += val
                continue

        idx += 1
    if is_part2:
        return reg['h']
    return mul_cnt


if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    instros = [x.strip() for x in data]

    reg = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
    }
    p1 = cpu(reg, instros, False)
    print(f"[Part1] : {p1}")

    reg = {
        'a': 1,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
    }
    p2 = cpu(reg, instros, True)
    print(f"[Part2] : {p2}")
