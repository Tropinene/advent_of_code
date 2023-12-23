def solveB(nums):
    seen = set([0])
    f = 0
    while True:
        for d in nums:
            f += d
            if f in seen:
                return f
            seen.add(f)
        print(f)


if __name__ == '__main__':
    frequency = open('input.txt', 'r').readlines()
    frequency = [int(x) for x in frequency]

    p1 = sum(frequency)
    print(f"[Part1] : {p1}")

    seen, cur = {0}, 0
    while True:
        for f in frequency:
            cur += f
            if cur in seen:
                print(f"[Part2] : {cur}")
                quit()
            seen.add(cur)