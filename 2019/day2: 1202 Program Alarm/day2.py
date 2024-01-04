import copy


def cal(lst):
    for idx in range(0, len(lst), 4):
        if lst[idx] == 1:
            pos1, pos2, save_pos = lst[idx+1], lst[idx+2], lst[idx+3]
            lst[save_pos] = lst[pos1] + lst[pos2]
        elif lst[idx] == 2:
            pos1, pos2, save_pos = lst[idx+1], lst[idx+2], lst[idx+3]
            lst[save_pos] = lst[pos1] * lst[pos2]
        elif lst[idx] == 99:
            break
    return lst[0]


if __name__ == "__main__":
    data  = open("input.txt", "r").readline().strip()
    lst = data.split(",")
    lst = [int(x) for x in lst]
    lst2 = copy.deepcopy(lst)

    lst[1], lst[2] = 12, 2
    print(f"[Part1] : {cal(lst)}")

    for n in range(100):
        for v in range(100):
            tmp = copy.deepcopy(lst2)
            lst2[1], lst2[2] = n, v
            if cal(lst2) == 19690720:
                print(f"[Part2] : {n * 100 + v}")
                quit()
            lst2 = tmp
