# part1: sum the difference between the largest value and the smallest value in every rows.
# part2: each has a pair of numbers which can be divisible. sum up the quotient.

import re


def find_divisible_pair(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] % nums[i] == 0:
                return nums[j] // nums[i]

    return 0


if __name__ == '__main__':
    lines = open('input.txt', 'r').readlines()
    p1, p2 = 0, 0
    for line in lines:
        matches = re.findall(r'\d+', line.strip())
        matches = list(map(int, matches))
        matches.sort()
        p1 += matches[-1] - matches[0]
        p2 += find_divisible_pair(matches)
    print(f"[Part1] : {p1}")
    print(f"[Part2] : {p2}")
