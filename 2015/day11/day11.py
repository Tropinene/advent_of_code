def check1(s):
    cnt = 1
    for i in range(1, len(s)):
        if ord(s[i - 1]) == ord(s[i]) - 1:
            cnt += 1
            if cnt == 3:
                return True
        else:
            cnt = 1
    return False


def check2(s):
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    return True


def check3(s):
    flag = True
    cnt = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            if flag:
                cnt += 1
                if cnt == 2:
                    return True
            flag = not flag
        else:
            flag = True
    return False


def increase(s):
    flag = True
    l = len(s)

    tmp = list(s)
    while flag:
        l -= 1
        if tmp[l] == 'z':
            tmp[l] = 'a'
        else:
            tmp[l] = chr(ord(tmp[l]) + 1)
            flag = False
    return ''.join(tmp)


if __name__ == '__main__':
    s = "cqjxjnds"

    while True:
        if check1(s) and check2(s) and check3(s):
            break
        else:
            s = increase(s)

    print(f'[Part1] : {s}')

    s = increase(s)
    while True:
        if check1(s) and check2(s) and check3(s):
            break
        else:
            s = increase(s)
    print(f'[Part2] : {s}')
