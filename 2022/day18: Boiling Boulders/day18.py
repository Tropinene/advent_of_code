def count_area(cubes: list) -> int:
    area = 6 * len(cubes)

    for i in range(len(cubes)):
        for j in range(i, len(cubes)):
            if sum(abs(a - b) for a, b in zip(cubes[i], cubes[j])) == 1:
                area -= 2
    return area


def main():
    cubes = [line.strip() for line in open('input.txt', 'r').readlines()]
    cubes = [list(map(int, s.split(','))) for s in cubes]

    p1 = count_area(cubes)
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()
