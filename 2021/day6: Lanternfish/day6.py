def _give_birth_memo(cur, limit, memo=None):
    if memo is None:
        memo = {}
    if cur >= limit:
        return 0
    if cur in memo:
        return memo[cur]

    cnt = 0
    for i in range(cur + 8, limit, 7):
        cnt += 1
        cnt += _give_birth_memo(i + 1, limit, memo)

    memo[cur] = cnt
    return cnt


def give_birth(cur, limit):
    cnt = 0
    for i in range(cur, limit, 7):
        cnt += 1
        cnt += _give_birth_memo(i+1, limit)
    return cnt


def main():
    timers = [int(x) for x in open('input.txt', 'r').readline().split(',')]

    p1 = len(timers)
    for i in timers:
        p1 += give_birth(i, 80)
    print(f"[Part1] : {p1}")

    p2 = len(timers)
    for i in timers:
        p2 += give_birth(i, 256)
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()