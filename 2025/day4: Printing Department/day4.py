import copy

def count_around_rolls(x: int, y: int, grid: list[list[str]]) -> int:
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                if grid[i][j] == '@':
                    count += 1
    return count-1 if grid[x][y] == '@' else count

def solve_part1(grid: list[list[str]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                if count_around_rolls(i, j, grid) < 4:
                    count += 1
    return count

def solve_part2(grid: list[list[str]]) -> int:
    grid2 = copy.deepcopy(grid)
    total_removed = 0
    
    while True:
        removed_this_round = 0
        grid_snapshot = copy.deepcopy(grid2)
        rows = len(grid_snapshot)
        cols = len(grid_snapshot[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid_snapshot[i][j] == '@':
                    if count_around_rolls(i, j, grid_snapshot) < 4:
                        grid2[i][j] = '.'
                        removed_this_round += 1
        
        if removed_this_round == 0:
            break
        total_removed += removed_this_round

    return total_removed

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        grid.append(list(line.strip()))

    print(f"[Part1] : {solve_part1(grid)}")
    print(f"[Part2] : {solve_part2(grid)}")