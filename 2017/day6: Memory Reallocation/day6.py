import copy


def reallocate(banks, is_part2):
    check = [banks]
    num_banks, step = len(banks), 0

    tmp = copy.deepcopy(banks)
    while True:
        tie_bank_idx, spread = choose(tmp)
        for idx in range(1, num_banks):
            if tmp[tie_bank_idx] == 0:
                break
            tmp[(tie_bank_idx+idx)%num_banks] += spread
            tmp[tie_bank_idx] -= spread
        step += 1
        if tmp in check:
            break
        check.append(copy.deepcopy(tmp))

    if not is_part2:
        return step
    else:
        first_appear = check.index(tmp)
        return step - first_appear


def choose(lst):
    tmp = copy.deepcopy(lst)
    tmp.sort(reverse=True)
    max_idx = lst.index(tmp[0])
    spread = lst[max_idx] // (len(lst)-1)
    return max_idx, max(spread, 1)


if __name__ == '__main__':
    data = open('input.txt', 'r').readline().strip().split()
    data = [int(x) for x in data]

    print(f"[Part1] : {reallocate(data, False)}")
    print(f"[Part2] : {reallocate(data, True)}")