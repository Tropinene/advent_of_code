import sys

# 提高递归限制以防万一
# sys.setrecursionlimit(2000)

def solve():
    # 从 input.txt 读取输入
    try:
        with open("input.txt", "r") as f:
            grid = [line.strip() for line in f]
    except FileNotFoundError:
        print("错误：未找到 input.txt 文件。")
        return

    R = len(grid)
    C = len(grid[0])

    # 1. 寻找起点 'S'
    start_r, start_c = -1, -1
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                start_r, start_c = r, c
                break
        if start_r != -1:
            break

    # 管道连接定义: (dr, dc) 是连接的方向
    connections = {
        '|': [(-1, 0), (1, 0)],    # 上, 下
        '-': [(0, -1), (0, 1)],    # 左, 右
        'L': [(-1, 0), (0, 1)],    # 上, 右
        'J': [(-1, 0), (0, -1)],   # 上, 左
        '7': [(1, 0), (0, -1)],    # 下, 左
        'F': [(1, 0), (0, 1)],     # 下, 右
        '.': [],                   # 地面，无连接
        'S': [(-1, 0), (1, 0), (0, -1), (0, 1)] # S可能连接所有方向，稍后确定
    }

    # 2. 找到主循环
    
    # 确定 'S' 的实际管道类型
    s_neighbors = []
    possible_s_pipes = []
    
    # 检查 S 的四个方向，找出可以连接到 S 的邻居
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = start_r + dr, start_c + dc
        if 0 <= r < R and 0 <= c < C:
            pipe = grid[r][c]
            # 检查邻居的连接是否可以回到 (start_r, start_c)
            # 例如: 如果 S 在 N 方向有一个 '|'，'|'的连接是(下, 上)，(下)是回到 S 的方向
            connects_back = False
            if pipe in connections:
                # 检查 (dr, dc) 的反向 (-dr, -dc) 是否在邻居管道的连接方向中
                if (-dr, -dc) in connections[pipe]:
                    s_neighbors.append((r, c))
                    possible_s_pipes.append((dr, dc))
    
    # 根据连接的两个方向确定 S 实际是什么管道
    # 我们可以通过其连接的方向来推断 S 的类型。
    # 这一步不是 Part 1 必需的，但对 Part 2 射线投射算法很有用。
    # 两个连接的方向
    dir1, dir2 = possible_s_pipes
    
    # 确保 dir1 和 dir2 有序，方便查找
    # 优先顺序：上(-1, 0) > 下(1, 0) > 左(0, -1) > 右(0, 1)
    if dir1[0] < dir2[0] or (dir1[0] == dir2[0] and dir1[1] < dir2[1]):
        pass
    else:
        dir1, dir2 = dir2, dir1

    # 所有的管道类型及其连接方向 (有序)
    pipe_types = {
        ((-1, 0), (1, 0)): '|',
        ((0, -1), (0, 1)): '-',
        ((-1, 0), (0, 1)): 'L',
        ((-1, 0), (0, -1)): 'J',
        ((1, 0), (0, -1)): '7',
        ((1, 0), (0, 1)): 'F',
    }

    s_pipe_type = pipe_types.get((dir1, dir2), 'S') # 找不到就还是 'S'

    # 使用 BFS/DFS 或简单迭代来遍历循环并记录路径
    loop_path = [(start_r, start_c)]
    
    # 从 S 的一个邻居开始
    if not s_neighbors:
        # 找不到邻居，说明 S 不在循环中 (不应该发生)
        part1_result = 0
        loop_set = set()
    else:
        # 从第一个邻居开始
        curr_r, curr_c = s_neighbors[0]
        prev_r, prev_c = start_r, start_c
        
        while (curr_r, curr_c) != (start_r, start_c):
            loop_path.append((curr_r, curr_c))
            pipe = grid[curr_r][curr_c]
            
            # 找到下一个点
            next_r, next_c = -1, -1
            for dr, dc in connections[pipe]:
                r, c = curr_r + dr, curr_c + dc
                # 确保下一步不是上一个点
                if (r, c) != (prev_r, prev_c):
                    next_r, next_c = r, c
                    break
            
            # 更新 prev 和 curr
            prev_r, prev_c = curr_r, curr_c
            curr_r, curr_c = next_r, next_c

        loop_set = set(loop_path)
        part1_result = len(loop_path) // 2

    
    # 3. 第二部分：计算内部区域
    part2_result = 0
    
    # **射线投射算法**
    # 替换 S 的实际管道类型
    grid_list = [list(row) for row in grid]
    grid_list[start_r][start_c] = s_pipe_type
    
    # 遍历每个点
    for r in range(R):
        inside = False
        # 记录进入循环的 'L' 或 'F' 角，用于处理 'L---7' 和 'F---J' 的情况
        # 只有 '|', 'L-7', 'F-J' 构成真正的边界穿越
        # 'L-J' 和 'F-7' 不构成穿越，因为它们在同一侧进出
        # 我们可以只关注 '|' 和 'L', 'F' 角
        prev_corner = None # 用于 L 和 F
        
        for c in range(C):
            point = (r, c)
            char = grid_list[r][c]
            
            if point in loop_set:
                # 管道字符，根据其类型决定是否翻转 inside 状态
                if char == '|':
                    inside = not inside
                elif char == 'L':
                    prev_corner = 'L'
                elif char == 'F':
                    prev_corner = 'F'
                elif char == 'J':
                    # L...J 不构成穿越
                    if prev_corner == 'F': # F...J 构成穿越
                        inside = not inside
                    prev_corner = None
                elif char == '7':
                    # F...7 不构成穿越
                    if prev_corner == 'L': # L...7 构成穿越
                        inside = not inside
                    prev_corner = None
                elif char == '-':
                    # 忽略 '-'，因为它不影响穿越计数，由两端的角处理
                    pass
            else:
                # 非管道或不在主循环中的点
                if inside:
                    part2_result += 1

    # 4. 输出结果
    print(f"[Part1]: {part1_result}")
    print(f"[Part2]: {part2_result}")


if __name__ == "__main__":
    solve()