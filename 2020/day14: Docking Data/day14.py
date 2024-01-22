import re
from itertools import product

from typing import List


def parse_file(is_part2: bool) -> (List[List[tuple]], List[List[tuple]]):
    lines = open('input.txt', 'r').read()

    lines_list = lines.split("mask = ")[1:]
    mems, masks = [], []
    for line in lines_list:
        tmp = line.split('\n')
        mask_str = tmp[0]
        mask = []
        for idx, c in enumerate(mask_str):
            if is_part2:
                if c != '0':
                    mask.append((idx, c))
            else:
                if c != 'X':
                    mask.append((idx, c))
        masks.append(mask)

        mem = []
        for ins in tmp[1:]:
            if ins:
                match = re.findall(r'\d+', ins)
                mem.append((int(match[0]), int(match[1])))
        mems.append(mem)
    return masks, mems


def generate_values(input_str: str) -> List[int]:
    x_count = input_str.count('X')
    results = []
    for combination in product(range(2), repeat=x_count):
        temp_str = input_str
        for binary_digit in combination:
            temp_str = temp_str.replace('X', str(binary_digit), 1)
        value = int(temp_str, 2)
        results.append(value)
    return results


def main():
    masks, allmems = parse_file(False)

    # Part 1
    men_set_part1 = {}
    for idx in range(len(masks)):
        mask, mems = masks[idx], allmems[idx]

        for (men, value) in mems:
            binary_list = list(bin(value)[2:].zfill(36))
            for (pos, bit) in mask:
                binary_list[pos] = bit
            men_set_part1[men] = int(''.join(binary_list), 2)

    p1 = sum(men_set_part1.values())
    print(f"[Part1] : {p1}")

    # Part 2
    masks, allmems = parse_file(True)
    men_set_part2 = {}
    for idx in range(len(masks)):
        mask, mems = masks[idx], allmems[idx]

        for (men, value) in mems:
            men_list = list(bin(men)[2:].zfill(36))
            for (pos, bit) in mask:
                men_list[pos] = bit
            modify_addrs = generate_values(''.join(men_list))
            for addr in modify_addrs:
                men_set_part2[addr] = value

    p2 = sum(men_set_part2.values())
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
