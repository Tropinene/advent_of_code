# a cpu with 4 registers and has instruction of [cpy inc dec jnz]
# part1: all registers' default value is 0
# part2: register 'c' default value is 1

def cpu(reg):
    instros = open("input.txt", "r").readlines()
    l, idx = len(instros), 0

    while idx < l:
        instro = instros[idx]
        lst = instro.split()
        if lst[0] == 'cpy':
            if lst[1].isdigit():
                reg[lst[2]] = int(lst[1])
            else:
                reg[lst[2]] = reg[lst[1]]
            idx += 1
        elif lst[0] == 'inc':
            reg[lst[1]] += 1
            idx += 1
        elif lst[0] == 'dec':
            reg[lst[1]] -= 1
            idx += 1
        elif lst[0] == 'jnz':
            if lst[1].isdigit():
                tmp = int(lst[1])
            else:
                tmp = reg[lst[1]]
            if tmp != 0:
                idx += int(lst[2])
            else:
                idx += 1
    return reg


if __name__ == "__main__":
    reg = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
    }
    reg = cpu(reg)
    print(f"[Part1] : {reg['a']}")

    reg = {
        'a': 0,
        'b': 0,
        'c': 1,
        'd': 0,
    }
    reg = cpu(reg)
    print(f"[Part1] : {reg['a']}")