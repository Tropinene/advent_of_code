import re


def parse_file():
    lines = open('input.txt', 'r').read()

    lines_list = lines.split("mask = ")[1:]
    mems, masks = [], []
    for line in lines_list:
        tmp = line.split('\n')
        mask_str = tmp[0]
        mask = []
        for idx, c in enumerate(mask_str):
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


def main():
    masks, allmems = parse_file()

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


if __name__ == '__main__':
    main()
