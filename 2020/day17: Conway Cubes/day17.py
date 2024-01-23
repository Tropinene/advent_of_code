import itertools


def get_neighbors(coord, dimensions):
    offsets = list(itertools.product([-1, 0, 1], repeat=dimensions))
    offsets.remove((0,) * dimensions)
    neighbors = [tuple(c + offset[i] for i, c in enumerate(coord)) for offset in offsets]
    return neighbors


def get_neighbors_4d(coord):
    offsets = list(itertools.product([-1, 0, 1], repeat=4))
    offsets.remove((0, 0, 0, 0))
    neighbors = []
    for offset in offsets:
        neighbors.append((coord[0] + offset[0], coord[1] + offset[1], coord[2] + offset[2], coord[3] + offset[3]))
    return neighbors


def simulate_cycle(active_cubes: set, get_neighbors_func) -> set:
    neighbor_counts = {}
    for cube in active_cubes:
        for neighbor in get_neighbors_func(cube):
            if neighbor not in neighbor_counts:
                neighbor_counts[neighbor] = 1
            else:
                neighbor_counts[neighbor] += 1
    
    new_active_cubes = set()
    for cube, count in neighbor_counts.items():
        if count == 3 or (count == 2 and cube in active_cubes):
            new_active_cubes.add(cube)
    
    return new_active_cubes


def initialize_cubes(input_file: str, dimensions: int) -> set:
    active_cubes = set()
    with open(input_file, 'r') as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                if char == '#':
                    coordinates = (x, y) + (0,) * (dimensions - 2)
                    active_cubes.add(coordinates)
    return active_cubes


def main():
    active_cubes = initialize_cubes('input.txt', 3)
    for _ in range(6):
        active_cubes = simulate_cycle(active_cubes, lambda coord: get_neighbors(coord, 3))

    print(f"[Part1] : {len(active_cubes)}")

    active_cubes = initialize_cubes('input.txt', 4)
    for _ in range(6):
        active_cubes = simulate_cycle(active_cubes, lambda coord: get_neighbors_4d(coord))

    print(f"[Part2] : {len(active_cubes)}")


if __name__ == "__main__":
    main()
