import copy
from typing import List


def solve_part1(decimals: List[str]) -> int:
    l_decimal = len(decimals[0])
    gamma_lst, epsilon_lst = [], []
    for idx in range(l_decimal):
        cnt = sum(decimal[idx] == '1' for decimal in decimals)
        if cnt * 2 >= len(decimals):
            gamma_lst.append('1')
            epsilon_lst.append('0')
        else:
            gamma_lst.append('0')
            epsilon_lst.append('1')
    gamma = int(''.join(gamma_lst), 2)
    epsilon = int(''.join(epsilon_lst), 2)
    return gamma * epsilon


def count(datas: List[str], is_most_common: bool, idx: int) -> str:
    cnt = sum(decimal[idx] == '1' for decimal in datas)
    gt = cnt * 2 >= len(datas)
    if gt == is_most_common:
        return '1'
    else:
        return '0'


def solve_part2(decimals: List[str]) -> int:
    idx, o2 = 0, copy.deepcopy(decimals)
    while len(o2) > 1:
        remain_char = count(o2, True, idx)
        o2 = [line for line in o2 if line[idx] == remain_char]
        idx += 1

    idx, co2 = 0, copy.deepcopy(decimals)
    while len(co2) > 1:
        remain_char = count(co2, False, idx)
        co2 = [line for line in co2 if line[idx] == remain_char]
        idx += 1
    return int(o2[0], 2) * int(co2[0], 2)


def main():
    decimals = [x.strip() for x in open('input.txt', 'r').readlines()]

    print(f"[Part1] : {solve_part1(decimals)}")
    print(f"[Part2] : {solve_part2(decimals)}")


if __name__ == '__main__':
    main()
