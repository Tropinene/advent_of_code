def parse_file():
    lines = open('input.txt', 'r').read()
    part1, part2 = lines.split('\n\n')
    part1, part2 = part1.split('\n'), part2.split('\n')

    dots, folds = [], []
    for line in part1:
        x, y = line.strip().split(',')
        dots.append((int(x), int(y)))

    for line in part2:
        core = line.strip().split()[-1]
        x, y = core.split('=')
        folds.append((x, int(y)))
    return dots, folds


def fold_paper(axis, line, dots):
    new_dots = []

    for x, y in dots:
        if axis == 'x':
            if x > line:
                x = line - (x - line)
        else:
            if y > line:
                y = line - (y - line)
        if (x, y) not in new_dots:
            new_dots.append((x, y))
    return new_dots


def main():
    dots, folds = parse_file()

    axis, line = folds[0]
    dots = fold_paper(axis, line, dots)
    print(f"[Part1] : {len(dots)}")

    for fold in folds[1:]:
        dots = fold_paper(fold[0], fold[1], dots)
    print("[Part2]")
    for i in range(6):
        for j in range(40):
            if (j, i) in dots:
                print('█', end='')
            else:
                print(' ', end='')
        print()


if __name__ == '__main__':
    main()
