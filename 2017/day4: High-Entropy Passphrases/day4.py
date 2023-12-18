def count(data, is_part2):
    res = 0
    for line in data:
        lst = line.strip().split()
        check, is_no_duplicate = [], True
        for item in lst:
            if is_part2:
                tmp = list(item)
                tmp.sort()
                item = ''.join(tmp)
            if item in check:
                is_no_duplicate = False
                break
            else:
                check.append(item)
        if is_no_duplicate:
            res += 1
    return res


if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()

    p1 = count(data, False)
    print(f"[Part1] : {p1}")

    p2 = count(data, True)
    print(f"[Part1] : {p2}")
