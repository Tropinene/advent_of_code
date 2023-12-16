# the same cpu in day12 but add a new instruction tpl
# part1: a start with 7, what is the value of a after running

def cpu(reg):
    instros = open("input.txt", "r").readlines()
    l, idx = len(instros), 0

    while idx < l:
        instro = instros[idx]
        lst = instro.split()

        if lst[0] == 'cpy':
            if lst[1].isdigit() or lst[1][0] == '-':
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
                if lst[2].isdigit() or lst[2][0] == '-':
                    idx += int(lst[2])
                else:
                    idx += reg[lst[2]]
            else:
                idx += 1
        elif lst[0] == 'tgl':
            if lst[1].isdigit() or lst[1][0] == '-':
                offset = int(lst[1])
            else:
                offset = reg[lst[1]]
            if idx + offset < l:
                if instros[idx + offset].startswith('cpy'):
                    instros[idx + offset] = instros[idx + offset].replace('cpy', 'jnz')
                elif instros[idx + offset].startswith('jnz'):
                    instros[idx + offset] = instros[idx + offset].replace('jnz', 'cpy')
                elif instros[idx + offset].startswith('inc'):
                    instros[idx + offset] = instros[idx + offset].replace('inc', 'dec')
                elif instros[idx + offset].startswith('dec'):
                    instros[idx + offset] = instros[idx + offset].replace('dec', 'inc')
                elif instros[idx + offset].startswith('tgl'):
                    instros[idx + offset] = instros[idx + offset].replace('tgl', 'inc')
            idx += 1
    return reg


if __name__ == "__main__":
    reg = {
        'a': 7,
        'b': 0,
        'c': 0,
        'd': 0,
    }
    reg = cpu(reg)
    print(f"[Part1] : {reg['a']}")

    reg = {
        'a': 12,
        'b': 0,
        'c': 0,
        'd': 0,
    }
    reg = cpu(reg)
    print(f"[Part2] : {reg['a']}")