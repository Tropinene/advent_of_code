# cpu won't tell you how many registers it has
# part1: get the highest value in all registers
# part2: get the highest value during the instruction

def is_condition(regs, condition):
    lst = condition.strip().split()
    if not regs.get(lst[0]):
        regs[lst[0]] = 0
    if lst[1] == '>' and regs[lst[0]] > int(lst[2]):
        return True
    elif lst[1] == '>=' and regs[lst[0]] >= int(lst[2]):
        return True
    elif lst[1] == '==' and regs[lst[0]] == int(lst[2]):
        return True
    elif lst[1] == '!=' and regs[lst[0]] != int(lst[2]):
        return True
    elif lst[1] == '<' and regs[lst[0]] < int(lst[2]):
        return True
    elif lst[1] == '<=' and regs[lst[0]] <= int(lst[2]):
        return True
    return False


def operate(regs, operation, max_value):
    lst = operation.strip().split()
    if not regs.get(lst[0]):
        regs[lst[0]] = 0
    if lst[1] == 'inc':
        regs[lst[0]] += int(lst[2])
    elif lst[1] == 'dec':
        regs[lst[0]] -= int(lst[2])

    return max(max_value, regs[lst[0]])


if __name__ == '__main__':
    instructions = open('input.txt', 'r').readlines()

    regs, max_value = {}, -1
    for line in instructions:
        operation, condition = line.strip().split(' if ')
        if is_condition(regs, condition):
            max_value = operate(regs, operation, max_value)
    values = list(regs.values())
    values.sort()
    print(f"[Part1] : {values[-1]}")
    print(f"[Part2] : {max_value}")