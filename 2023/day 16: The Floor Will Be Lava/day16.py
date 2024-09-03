def energize_tiles(grid):
    rows, cols = len(grid), len(grid[0])
    energized = [[False] * cols for _ in range(rows)]

    # 定义方向向量，顺序为：右(0,1), 下(1,0), 左(0,-1), 上(-1,0)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def next_direction(current_dir, mirror):
        if mirror == '/':
            return (3, 2, 1, 0)[current_dir]
        elif mirror == '\\':
            return (1, 0, 3, 2)[current_dir]
        return current_dir

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # 开始从左上角向右传播光束
    queue = [(0, 0, 0)]  # (row, col, direction)
    visited = set()  # 记录已经访问过的状态

    while queue:
        x, y, dir_index = queue.pop(0)

        while in_bounds(x, y):
            # 标记当前格子为激活
            energized[x][y] = True

            # 如果状态已经访问过，停止处理当前路径
            state = (x, y, dir_index)
            if state in visited:
                break
            visited.add(state)

            cell = grid[x][y]

            if cell == '.':
                pass  # 继续向当前方向移动
            elif cell in '/\\':
                dir_index = next_direction(dir_index, cell)  # 反射
            elif cell == '|':
                if dir_index in [1, 3]:  # 当前方向为垂直方向，继续前进
                    pass  # 继续直行
                else:  # 当前方向为水平方向，进行分裂
                    queue.append((x, y, 1))  # 向下
                    queue.append((x, y, 3))  # 向上
                    break
            elif cell == '-':
                if dir_index in [0, 2]:  # 当前方向为水平方向，继续前进
                    pass  # 继续直行
                else:  # 当前方向为垂直方向，进行分裂
                    queue.append((x, y, 0))  # 向右
                    queue.append((x, y, 2))  # 向左
                    break

            # 根据当前方向移动到下一个格子
            x += directions[dir_index][0]
            y += directions[dir_index][1]
    # 打印格子的状态图
    # for row in energized:
    #     for g in row:
    #         if g:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
    # 计算激活的格子数
    return sum(sum(row) for row in energized)


def main():
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    # 计算并打印激活的格子数
    result = energize_tiles(grid)
    print(f"[Part1] : {result}")


if __name__ == '__main__':
    main()
