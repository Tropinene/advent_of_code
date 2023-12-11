def get_factor(num):
    res = []
    end = int(num**0.5) + 1
    for i in range(1, end):
        if num % i == 0:
            res.append(i)
            if i != num//i:
                res.append(num//i)
    res.sort()
    return res


def get_part2(lst, num):
    for idx in range(len(lst)):
        if lst[idx] * 50 > num:
            return idx


if __name__ == '__main__':
    inp = 33100000
    num = 700000
    fin1, fin2 = False, False
    while True:
        if fin1 and fin2:
            break
        lst = get_factor(num)
        if not fin1 and sum(lst) * 10 > inp:
            print(f"[Part1] : {num}")
            fin1 = True

        idx = get_part2(lst, num)
        if not fin2 and sum(lst[idx:]) * 11 > inp:
            print(f"[Part2] : {num}")
            fin2 = True
        num += 1
