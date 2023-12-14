# input string consists of '.' and '#'
# you should follow four rulers to generate next line
# part1: count the number 0f '.' in 40 lines
# part2: count the number 0f '.' in 400000 lines

def safe(s, idx):
    if idx < 0 or idx == len(s):
        return True
    if s[idx] == '.':
        return True
    return False


def is_trap(s, idx):
    if not safe(s, idx-1) and not safe(s, idx) and safe(s, idx+1):
        return True
    if safe(s, idx-1) and not safe(s, idx) and not safe(s, idx+1):
        return True
    if not safe(s, idx-1) and safe(s, idx) and safe(s, idx+1):
        return True
    if safe(s, idx-1) and safe(s, idx) and not safe(s, idx+1):
        return True
    return False


def gen_new_line(s):
    res = []
    cnt = 0
    for i in range(len(s)):
        if is_trap(s, i):
            res.append('^')
        else:
            res.append('.')
            cnt += 1
    return ''.join(res), cnt


if __name__ == '__main__':
    line = open('input.txt', 'r').readline()

    p1 = 37
    for _ in range(39):
        line, n = gen_new_line(line)
        p1 += n

    print(f'[Part1] : {p1}')

    line = open('input.txt', 'r').readline()
    p2 = 37
    for _ in range(399999):
        line, n = gen_new_line(line)
        p2 += n

    print(f'[Part1] : {p2}')
