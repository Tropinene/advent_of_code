import itertools
import re


if __name__ == '__main__':
    towns = set()
    distances = {}

    data = open('input.txt', 'r').readlines()
    for line in data:
        town1, town2, distance = re.match(r'(\w+) to (\w+) = (\d+)', line.strip()).groups()
        towns.add(town1)
        towns.add(town2)
        town1, town2 = sorted((town1, town2))
        distances[(town1, town2)] = int(distance)

    options = []
    for order in itertools.permutations(towns):
        path = zip(order, order[1:])
        path_distances = [distances[tuple(sorted((town1, town2)))] for town1, town2 in path]
        total_distance = sum(path_distances)
        options.append(total_distance)

    print(f"[Part1] : {min(options)}")
    print(f"[Part2] : {max(options)}")