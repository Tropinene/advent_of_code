import itertools

def get_neighbors(cube):
    x, y, z = cube
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1)
    ]


def fill_holes(cubes: list):
    min_x, min_y, min_z = map(min, zip(*cubes))
    max_x, max_y, max_z = map(max, zip(*cubes))

    filled = set(tuple(cube) for cube in cubes)
    exterior = set()
    stack = [(min_x, min_y, min_z)]  # 从熔岩外部开始

    while stack:
        current = stack.pop()
        if current in exterior or current in filled:
            continue
        exterior.add(current)

        # 动态计算相邻的6个方向
        for neighbor in get_neighbors(current):
            if (min_x-1 <= neighbor[0] <= max_x+1 and
                    min_y-1 <= neighbor[1] <= max_y+1 and
                    min_z-1 <= neighbor[2] <= max_z+1):
                stack.append(neighbor)

    # 所有不在熔岩块和外部空气中的立方体就是内部的空气
    internal_air = {(x, y, z)
                    for x in range(min_x, max_x + 1)
                    for y in range(min_y, max_y + 1)
                    for z in range(min_z, max_z + 1)} - filled - exterior

    return [list(cube) for cube in filled | internal_air]


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

    p2 = count_area(fill_holes(cubes))
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
