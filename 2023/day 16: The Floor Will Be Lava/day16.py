def next_direction(current_dir, mirror):
    if mirror == '/':
        return (3, 2, 1, 0)[current_dir]
    elif mirror == '\\':
        return (1, 0, 3, 2)[current_dir]
    return current_dir


def energize_tiles(grid, start_x, start_y, start_dir):
    rows, cols = len(grid), len(grid[0])
    energized = [[False] * cols for _ in range(rows)]

    # 定义方向向量，顺序为：右(0,1), 下(1,0), 左(0,-1), 上(-1,0)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 开始从指定位置传播光束
    queue = [(start_x, start_y, start_dir)]  # (row, col, direction)
    visited = set()  # 记录已经访问过的状态

    while queue:
        x, y, dir_index = queue.pop(0)

        while 0 <= x < rows and 0 <= y < cols:
            # 标记当前格子为激活
            energized[x][y] = True

            # 如果状态已经访问过，停止处理当前路径
            state = (x, y, dir_index)
            if state in visited:
                break
            visited.add(state)

            cell = grid[x][y]

            if cell in '/\\':
                dir_index = next_direction(dir_index, cell)  # 反射
            elif cell == '|':
                if dir_index in [0, 2]:  # 当前方向为水平方向，进行分裂
                    queue.append((x, y, 1))  # 向下
                    queue.append((x, y, 3))  # 向上
                    break
            elif cell == '-':
                if dir_index in [1, 3]:  # 当前方向为垂直方向，进行分裂
                    queue.append((x, y, 0))  # 向右
                    queue.append((x, y, 2))  # 向左
                    break

            # 根据当前方向移动到下一个格子
            x += directions[dir_index][0]
            y += directions[dir_index][1]

    # 计算激活的格子数
    return sum(sum(row) for row in energized)


def find_max_energized(grid):
    rows, cols = len(grid), len(grid[0])
    max_energized = 0

    # 从顶部边界开始
    for y in range(cols):
        for start_dir in range(4):
            max_energized = max(max_energized, energize_tiles(grid, 0, y, start_dir))

    # 从底部边界开始
    for y in range(cols):
        for start_dir in range(4):
            max_energized = max(max_energized, energize_tiles(grid, rows - 1, y, start_dir))

    # 从左侧边界开始
    for x in range(rows):
        for start_dir in range(4):
            max_energized = max(max_energized, energize_tiles(grid, x, 0, start_dir))

    # 从右侧边界开始
    for x in range(rows):
        for start_dir in range(4):
            max_energized = max(max_energized, energize_tiles(grid, x, cols - 1, start_dir))

    return max_energized


def main():
    grid = [line.strip() for line in open('input.txt', 'r').readlines()]

    result = energize_tiles(grid, 0, 0, 0)
    print(f"[Part1] : {result}")

    result = find_max_energized(grid)
    print(f"[Part2] : {result}")


if __name__ == '__main__':
    main()
