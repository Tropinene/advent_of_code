def check_valid(line):
    rule, pwd = line.split(':')
    times, word = rule.split()
    less, high = times.split('-')

    cnt = pwd.count(word)
    if int(less) <= cnt <= int(high):
        return True
    return False


def check_valid2(line):
    rule, pwd = line.split(':')
    times, word = rule.split()
    first, second = times.split('-')

    pwd = pwd.strip()
    check_str = pwd[int(first)-1] + pwd[int(second)-1]
    if check_str.count(word) == 1:
        return True
    return False


if __name__ == '__main__':
    lines = open('input.txt', 'r').readlines()

    p1, p2 = 0, 0
    for line in lines:
        if check_valid(line):
            p1 += 1
        if check_valid2(line):
            p2 += 1
    print(f"[Part1] : {p1}")
    print(f"[Part2] : {p2}")
