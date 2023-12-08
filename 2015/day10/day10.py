def LookSay(look_s):
    new_s = ''
    c = 0
    curr = s[0]
    for i in range(len(s)):
        if (i > 0 and s[i] != curr):
            new_s += f'{c}{s[i - 1]}'
            curr = s[i]
            c = 0
        c += 1
    new_s += f'{c}{curr}'
    return new_s


if __name__ == '__main__':
    s = "1113222113"

    for _ in range(40):
        s = LookSay(s)

    print(f'[Part1] : {len(s)}')

    # for _ in range(10):
    for _ in range(10):
        s = LookSay(s)
    print(f'[Part2] : {len(s)}')
