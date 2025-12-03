def create_directions(pos: tuple) -> list:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = []
    x, y = pos
    for dx, dy in dirs:
        res.append((x+dx, y+dy))
    return res

def step(current_plots: set, garden: list, h: int, w: int) -> set:
    next_points = set()
    for x, y in current_plots:
        next_steps = create_directions((x, y))
        for nx, ny in next_steps:
            if garden[nx % h][ny % w] != '#':
                next_points.add((nx, ny))
    return next_points

def find_S(garden) -> tuple:
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if garden[i][j] == 'S':
                return i, j
    return 0, 0

def solve_quadratic(y0, y1, y2, x):
    a = (y2 - 2 * y1 + y0) // 2
    b = y1 - y0 - a
    c = y0
    return a * x**2 + b * x + c

def main():
    with open('input.txt', 'r') as f:
        garden = [list(x.strip()) for x in f.readlines()]
    
    h = len(garden)
    w = len(garden[0])
    start = find_S(garden)

    reach_plots = {start}   
    for _ in range(64):
        reach_plots = step(reach_plots, garden, h, w)
    print(f"[Part1]: {len(reach_plots)}")


    total_steps = 26501365
    size = h
    remainder = total_steps % size
    
    current_plots = {start}
    y_values = []
    
    target_checkpoints = [remainder, remainder + size, remainder + size * 2]
    max_steps = target_checkpoints[-1]
    
    for i in range(1, max_steps + 1):
        current_plots = step(current_plots, garden, h, w)
        if i in target_checkpoints:
            y_values.append(len(current_plots))
            
    grid_count = total_steps // size
    result = solve_quadratic(y_values[0], y_values[1], y_values[2], grid_count)
    
    print(f"[Part2]: {result}")

if __name__ == '__main__':
    main()