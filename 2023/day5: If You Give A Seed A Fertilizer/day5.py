def mapping(target: int, relation: list) -> int:
    for line in relation:
        dest, source, _range = (int(x) for x in line.split())
        if source <= target <= source + _range:
            return dest + target - source
    return target


def main():
    maps = open('input.txt', 'r').read().split('\n\n')
    seeds = maps[0]
    maps = maps[1:]
    final_maps = []
    for m in maps:
        m = m.split('\n')[1:]
        final_maps.append(m)

    num_seeds = [int(x) for x in seeds[7:].split()]
    min_location = 10000000000

    for s in num_seeds:
        tmp = s
        for m in final_maps:
            tmp = mapping(tmp, m)
        min_location = min(min_location, tmp)
    print(f"[Part1] : {min_location}")


if __name__ == '__main__':
    main()
