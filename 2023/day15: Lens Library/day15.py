def _hash(s: str) -> int:
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    return value


def process_step(step, lens_dict):
    if '=' in step:
        lens, focal = step.split('=')
        h = _hash(lens)
        if h not in lens_dict:
            lens_dict[h] = [(lens, focal)]
        else:
            exist = False
            for i, entry in enumerate(lens_dict[h]):
                if entry[0] == lens:
                    lens_dict[h][i] = (lens, focal)
                    exist = True
                    break
            if not exist:
                lens_dict[h].append((lens, focal))
    else:
        lens = step[:-1]
        for key, entries in list(lens_dict.items()):
            lens_dict[key] = [entry for entry in entries if entry[0] != lens]


def calculate_part2(lens_dict):
    p2 = 0
    for key, entries in lens_dict.items():
        for i, entry in enumerate(entries):
            p2 += (int(key) + 1) * (i + 1) * int(entry[1])
    return p2


def main():
    data = open('input.txt', 'r').readline()
    steps = data.strip().split(',')

    p1 = sum(_hash(step) for step in steps)
    print(f"[Part1] : {p1}")

    lens_dict = {}
    for step in steps:
        process_step(step, lens_dict)

    p2 = calculate_part2(lens_dict)
    print(f"[Part2] : {p2}")


if __name__ == "__main__":
    main()
