def bubble_sort(my_list: list):
    n = len(my_list)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not compare(my_list[j], my_list[j + 1]):
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


def compare(left: list, right: list) -> bool:
    min_len = min(len(left), len(right))
    for idx in range(min_len):
        if left[idx] == right[idx]:
            continue

        if type(left[idx]) == type(right[idx]):
            if type(left[idx]) == int:
                return left[idx] < right[idx]
            else:
                return compare(left[idx], right[idx])
        else:
            tmp = []
            if type(left[idx]) == int:
                tmp.append(left[idx])
                if tmp == right[idx]:
                    continue
                else:
                    return compare(tmp, right[idx])
            else:
                tmp.append(right[idx])
                if tmp == left[idx]:
                    continue
                else:
                    return compare(left[idx], tmp)

    return len(left) < len(right)


def main():
    data = open('input.txt', 'r').read()
    pairs = data.split('\n\n')

    p1, p2_lst = 0, []
    for idx, pair in enumerate(pairs):
        str1, str2 = pair.split('\n')
        lst1, lst2 = eval(str1), eval(str2)
        p2_lst.append(lst1)
        p2_lst.append(lst2)
        if compare(lst1, lst2):
            p1 += 1 + idx
    print(f"[Part1] : {p1}")

    flag1, flag2 = eval("[[2]]"), eval("[[6]]")
    p2_lst.append(flag1)
    p2_lst.append(flag2)
    bubble_sort(p2_lst)
    p2 = (p2_lst.index(flag1) + 1) * (p2_lst.index(flag2) + 1)
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
