import hashlib


def rocks_map(filePath: str) -> list:
    lines = [line.strip() for line in open('input.txt', 'r').readlines()]
    char_matrix = list(map(list, lines))

    return char_matrix


def move_north(rocks: list) -> list:
    for row, line in enumerate(rocks):
        for col, rock in enumerate(line):
            if rock != 'O':
                continue

            tmp = row
            rocks[tmp][col] = '.'

            while tmp - 1 >= 0 and rocks[tmp - 1][col] == '.':
                tmp -= 1
            rocks[tmp][col] = rock

    return rocks


def move_south(rocks: list) -> list:
    for row, line in enumerate(reversed(rocks)):
        for col, rock in enumerate(line):
            if rock != 'O':
                continue

            tmp = len(rocks) - row - 1
            rocks[tmp][col] = '.'

            while tmp + 1 < len(rocks) and rocks[tmp + 1][col] == '.':
                tmp += 1
            rocks[tmp][col] = rock
    return rocks


def move_west(rocks: list) -> list:
    for row, line in enumerate(rocks):
        for col, rock in enumerate(line):
            if rock != 'O':
                continue

            tmp = col
            rocks[row][tmp] = '.'

            while tmp - 1 >= 0 and rocks[row][tmp - 1] == '.':
                tmp -= 1
            rocks[row][tmp] = rock
    return rocks


def move_east(rocks: list) -> list:
    for row, line in enumerate(rocks):
        for col, rock in enumerate(reversed(line)):
            if rock != 'O':
                continue

            tmp = len(line) - col - 1
            rocks[row][tmp] = '.'

            while tmp + 1 < len(line) and rocks[row][tmp + 1] == '.':
                tmp += 1
            rocks[row][tmp] = rock
    return rocks


def main():
    rocks = rocks_map('input.txt')
    newRocks = move_north(rocks)

    p1, l = 0, len(newRocks)
    for idx, rocks in enumerate(newRocks):
        p1 += rocks.count('O') * (l - idx)
    print(f'[Part1] : {p1}')

    rocks = rocks_map('input.txt')
    # md5s, break_symbols, first_repeat = [], '', 0
    for idx in range(10000000000):
        newRocks = move_north(rocks)
        newRocks = move_west(newRocks)
        newRocks = move_south(newRocks)
        newRocks = move_east(newRocks)

        # rockStr = ''.join([''.join(sublist) for sublist in newRocks])
        # md5_hash = hashlib.md5(rockStr.encode('utf-8')).hexdigest()
        # if break_symbols == md5_hash:
        #     # print('break', idx, idx-first_repeat)
        #     break
        # if md5_hash in md5s and break_symbols == '':
        #     break_symbols = md5_hash
        #     first_repeat = idx
            # print(md5s)
            # break
        # md5s.append(md5_hash)
        # if idx % 1000000 == 0 and idx:
        #     print(idx)

        # last_five_elements = md5s[-3:]
        # if len(last_five_elements) == 3 and all(item == md5_hash for item in last_five_elements):
        #     print(idx)
        #     break
    # loop_times = (10000000000 - idx) % (idx - first_repeat)
    # for idx in range(loop_times):
    #     newRocks = move_north(newRocks)
    #     newRocks = move_west(newRocks)
    #     newRocks = move_south(newRocks)
    #     newRocks = move_east(newRocks)

    p2, l = 0, len(newRocks)
    for idx, rocks in enumerate(newRocks):
        p2 += rocks.count('O') * (l - idx)
    print(f'[Part2] : {p2}')


if __name__ == '__main__':
    main()
