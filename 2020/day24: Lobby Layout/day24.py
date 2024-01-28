def get_adjacent_tiles(x: int, y: int) -> list:
    return [
        (x + 1, y),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x, y - 1),
        (x + 1, y - 1),
    ]


def split_directions(input_str: str) -> list:
    directions, i = [], 0

    while i < len(input_str):
        if i + 1 < len(input_str) and input_str[i:i+2] in ['se', 'sw', 'nw', 'ne']:
            directions.append(input_str[i:i+2])
            i += 2
        else:
            directions.append(input_str[i])
            i += 1

    return directions


def flip_tile(tile: set, directions: list):
    moves = {
        'e': (1, 0),
        'se': (0, 1),
        'sw': (-1, 1),
        'w': (-1, 0),
        'nw': (0, -1),
        'ne': (1, -1),
    }

    x, y = 0, 0
    for direction in directions:
        dx, dy = moves[direction]
        x += dx
        y += dy

    if (x, y) in tile:
        tile.remove((x, y))
    else:
        tile.add((x, y))


def flip_by_day(tile: set) -> set:
    new_tile, black_tiles_to_check = set(), set()

    for (x, y) in tile:
        black_neighbors = sum((nx, ny) in tile for nx, ny in get_adjacent_tiles(x, y))
        if 0 < black_neighbors <= 2:
            new_tile.add((x, y))
        black_tiles_to_check.update(get_adjacent_tiles(x, y))

    for (x, y) in black_tiles_to_check:
        black_neighbors = sum((nx, ny) in tile for nx, ny in get_adjacent_tiles(x, y))
        if black_neighbors == 2:
            new_tile.add((x, y))

    return new_tile


def main():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]

    tile = set()
    for line in lines:
        directions = split_directions(line)
        flip_tile(tile, directions)

    print(f"[Part1] : {len(tile)}")

    for _ in range(100):
        tile = flip_by_day(tile)
    print(f"[Part2] : {len(tile)}")


if __name__ == "__main__":
    main()
