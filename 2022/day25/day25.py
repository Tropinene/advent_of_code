def convert(s):
    l = len(s)
    res = 0
    for idx, i in enumerate(s):
        if i == '-':
            factor = -1
        elif i == '=':
            factor = -2
        else:
            factor = int(i)
        res += factor * (5 ** (l-idx-1))
    return res


def tran2SNAFU(num):
    res = ""

    while num:
        rem = num % 5
        num //= 5

        if rem <= 2:
            res = str(rem) + res
        else:
            if rem == 3:
                res = "=" + res
            elif rem == 4:
                res = "-" + res
            num += 1
    return res

if __name__ == '__main__':
    lines = open('input.txt', 'r').readlines()
    sum = 0
    for line in lines:
        sum += convert(line.strip())
    print(f"[Part1] : {tran2SNAFU(sum)}")