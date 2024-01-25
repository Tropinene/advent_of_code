def chunk_check(s: str) -> (str, bool):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    lst = []
    for i in s:
        if pairs.get(i):
            if lst[-1] == pairs[i]:
                lst.pop()
            else:
                return i, False
        else:
            lst.append(i)

    if len(lst) > 0:
        return ''.join(lst), True
    else:
        return None, False


def main():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    scores2 = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    p1, p2 = 0, []
    for line in lines:
        c, is_incomplete = chunk_check(line)
        if c and not is_incomplete:
            p1 += scores[c]
        if is_incomplete:
            tmp = 0
            for i in c[::-1]:
                tmp = tmp * 5 + scores2[i]
            p2.append(tmp)
    print(f"[Part1] : {p1}")

    p2.sort()
    idx = len(p2) // 2
    print(f"[Part2] : {p2[idx]}")


if __name__ == '__main__':
    main()
