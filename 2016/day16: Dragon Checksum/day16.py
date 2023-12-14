# step 0: input a
# step 1: b = reverse(a) then 0 to 1, 1 to 0
# step 2: res = a + '0' + b, if not match the requirement. Repeat and slice
# step 3: calculate checksum.
#   1. split into 2 characters, 11,00 => 1, 01,10 => 0
#   2. if checksum is even, repeat.
# part1: length = 272, a = "10010000000110000", checksum = ?
# part2: length = 35651584

def get_b(s):
    res = []
    s = s[::-1]
    for i in s:
        if i == '0':
            res.append('1')
        else:
            res.append('0')
    return ''.join(res)


def checksum(s):
    res = []
    for i in range(0, len(s), 2):
        if s[i] != s[i+1]:
            res.append('0')
        else:
            res.append('1')
    return ''.join(res)


if __name__ == '__main__':
    length, a = 272, "10010000000110000"
    while len(a) < length:
        b = get_b(a)
        a = a + '0' + b
    res = a[:length]
    check = checksum(res)
    while len(check) % 2 == 0:
        check = checksum(check)
    print(f'[Part1] : {check}')

    length, a = 35651584, "10010000000110000"
    while len(a) < length:
        b = get_b(a)
        a = a + '0' + b
    res = a[:length]
    check = checksum(res)
    while len(check) % 2 == 0:
        check = checksum(check)
    print(f'[Part2] : {check}')
