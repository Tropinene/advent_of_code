def cal(register):
    data = open("input.txt", "r").readlines()
    idx = 0
    while idx < len(data):
        instruction = data[idx].strip()
        lst = instruction.split()
        if lst[0] == "inc":
            register[lst[1]] += 1
            idx += 1
        elif lst[0] == "tpl":
            register[lst[1]] *= 3
            idx += 1
        elif lst[0] == "hlf":
            register[lst[1]] = int(register[lst[1]] / 2)
            idx += 1
        elif lst[0] == "jmp":
            idx += int(lst[1])
        elif lst[0] == "jie":
            op = lst[1].strip(',')
            if register[op] % 2 == 0:
                idx += int(lst[2])
            else:
                idx += 1
        elif lst[0] == "jio":
            op = lst[1].strip(',')
            if register[op] == 1:
                idx += int(lst[2])
            else:
                idx += 1
        else:
            print("[ERROR] : Invalid!")
            break
    return register


if __name__ == "__main__":
    reg = {
        'a': 0,
        'b': 0,
    }
    p1 = cal(reg)
    print(f"[Part1] : {p1['b']}")

    reg = {
        'a': 1,
        'b': 0,
    }
    p2 = cal(reg)
    print(f"[Part2] : {p2['b']}")


