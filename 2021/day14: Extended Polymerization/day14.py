from collections import Counter


def parse_file():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    origin_str = lines[0]
    rules = {}
    for line in lines[2:]:
        a, b = line.split(' -> ')
        rules[a] = b
    return origin_str, rules


def solve(s: str, rules: dict, round: int) -> int:
    for cnt in range(round):
        if cnt % 5 == 0:
            print(cnt)
        check_lst = [s[idx] + s[idx + 1] for idx in range(len(s) - 1)]

        new_s_list = []
        idx = 1
        for c in check_lst:
            insert = rules.get(c)
            new_s_list.append(c[0] + insert)
            idx += 2
        new_s_list.append(s[-1])
        s = "".join(new_s_list)

    char_count = Counter(s)
    max_cnt = char_count.most_common()[0][1]
    min_cnt = char_count.most_common()[-1][1]
    return max_cnt - min_cnt


def main():
    s, rules = parse_file()

    print(f"[Part1] : {solve(s, rules, 10)}")
    print(f"[Part2] : {solve(s, rules, 40)}")


if __name__ == '__main__':
    main()
