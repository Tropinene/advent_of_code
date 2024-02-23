def manhattan_distance(point1: tuple, point2: tuple) -> bool:
    return sum(abs(a - b) for a, b in zip(point1, point2))


def find_parent(group_parents: dict, point: tuple):
    if group_parents[point] == point:
        return point
    return find_parent(group_parents, group_parents[point])


def union(group_parents: dict, point1: tuple, point2: tuple):
    parent1 = find_parent(group_parents, point1)
    parent2 = find_parent(group_parents, point2)
    group_parents[parent1] = parent2


def count_groups(coordinates: list) -> int:
    group_parents = {point: point for point in coordinates}

    for i, point1 in enumerate(coordinates):
        for j, point2 in enumerate(coordinates):
            if i != j and manhattan_distance(point1, point2) <= 3:
                union(group_parents, point1, point2)

    unique_groups = set(find_parent(group_parents, point) for point in coordinates)
    return len(unique_groups)


def parse_file() -> list:
    return [tuple(map(int, line.strip().split(','))) for line in open('input.txt', 'r').readlines()]


def main():
    coordinates = parse_file()
    result = count_groups(coordinates)
    print(f"[Part1] : {result}")


if __name__ == '__main__':
    main()
