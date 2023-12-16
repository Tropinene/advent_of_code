# generate by chatgpt-3.5

from collections import deque
from itertools import permutations


def read_map_from_file(file_path):
    with open(file_path, 'r') as file:
        map_data = [line.strip() for line in file]
    return map_data


def find_all_coordinates(map_data):
    all_coordinates_list = []

    for num in "01234567":
        for i in range(len(map_data)):
            for j in range(len(map_data[0])):
                if map_data[i][j] == num:
                    all_coordinates_list.append((i, j))

    return all_coordinates_list


def shortest_path(map_data, start, end):
    def neighbors(point):
        x, y = point
        return [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]

    def is_valid(point):
        x, y = point
        return 0 <= x < len(map_data) and 0 <= y < len(map_data[0]) and map_data[x][y] != '#'

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        current, steps = queue.popleft()

        if current == end:
            return steps  # Found the shortest path

        for neighbor in neighbors(current):
            if is_valid(neighbor) and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))


def find_shortest_path(map_data, is_part2):
    all_coordinates_list = find_all_coordinates(map_data)
    start_coordinates = all_coordinates_list[0]
    rest_coordinates = all_coordinates_list[1:]

    min_path_length = float('inf')

    for permuted_coordinates in permutations(rest_coordinates):
        current_path_length = 0
        current_location = start_coordinates

        for target_coordinates in permuted_coordinates:
            current_path_length += shortest_path(map_data, current_location, target_coordinates)
            current_location = target_coordinates

        if is_part2:
            current_path_length += shortest_path(map_data, current_location, start_coordinates)

        if current_path_length < min_path_length:
            min_path_length = current_path_length

    return min_path_length


if __name__ == '__main__':
    map_data = read_map_from_file('input.txt')
    p1 = find_shortest_path(map_data, False)
    print(f"[Part1] : {p1}")

    p2 = find_shortest_path(map_data, True)
    print(f"[Part2] : {p2}")

