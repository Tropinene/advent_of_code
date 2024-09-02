def read_file(f: str) -> list:
    with open(f, 'r') as file:
        instructions = [line.strip() for line in file]
    return instructions


def parse(instructions: list, reg: int) -> str:
    regs = {'a': reg, 'b': 0, 'c': 0, 'd': 0}

    idx, output = 0, ''
    while idx < len(instructions):
        ins = instructions[idx].split()
        if ins[0] == 'cpy':
            if ins[1].isdigit():
                regs[ins[2]] = int(ins[1])
            else:
                regs[ins[2]] = regs[ins[1]]
        elif ins[0] == 'inc':
            regs[ins[1]] += 1
        elif ins[0] == 'dec':
            regs[ins[1]] -= 1
        elif ins[0] == 'jnz':
            if ins[1].isdigit():
                tmp = int(ins[1])
            else:
                tmp = regs[ins[1]]
            if tmp != 0:
                idx += int(ins[2])
                continue
        elif ins[0] == 'out':
            output += str(regs[ins[1]])
        idx += 1
        if len(output) > 7:
            break
    return output


if __name__ == '__main__':
    fileName = 'input.txt'
    for a in range(1000):
        res = parse(read_file(fileName), a)
        # print(res)
        if res == '01010101':
            print(f"[Part1] : {a}")
            break
