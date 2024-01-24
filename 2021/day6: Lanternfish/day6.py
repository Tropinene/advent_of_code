def _give_birth(cur, limit):
    if cur >= limit:
        return 0
    cnt = 0
    for i in range(cur+8, limit, 7):
        # print(f"son:{i}")
        cnt += 1
        cnt += _give_birth(i+1, limit)
    return cnt

def give_birth(cur, limit):
    cnt = 0
    for i in range(cur, limit, 7):
        cnt += 1
        cnt += _give_birth(i+1, limit)
    return cnt
def main():
    timers = [int(x) for x in open('input.txt', 'r').readline().split(',')]

    p1 = len(timers)
    for i in timers:
        p1 += give_birth(i, 80)
    print(f"[Part1] : {p1}")

if __name__ == '__main__':
    main()
#         3
# day1    2
# day2    1
# day3    0
# day4    6   8
#   |
# day10   0   2
# day11   6   1   8
# day12   5   0   7
# day13   4   6   6
#   |
# day17   0   2   2
# day18   6   1   1   8
