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

            while tmp - 1 >= 0 and rocks[tmp-1][col] == '.':
                tmp -= 1
            rocks[tmp][col] = rock

    return rocks


def main():
    rocks = rocks_map('input.txt')
    newRocks = move_north(rocks)

    p1, l = 0, len(newRocks)
    for idx, rocks in enumerate(newRocks):
        p1 += rocks.count('O') * (l - idx)
    print(f'[Part1] : {p1}')


if __name__ == '__main__':
    main()