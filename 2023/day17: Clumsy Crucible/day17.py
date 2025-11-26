import heapq
import sys

def parse_input(filename):
    """读取并解析网格数据"""
    try:
        with open(filename, 'r') as f:
            # 将每个字符转换为整数
            grid = [[int(char) for char in line.strip()] for line in f]
        return grid
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        sys.exit(1)

def solve_dijkstra(grid, min_steps, max_steps):
    rows, cols = len(grid), len(grid[0])
    
    # 优先级队列: (heat_loss, r, c, dr, dc, consecutive_steps)
    # 起始点是 (0,0)，热量损失为 0。
    # 我们不仅要推入起点，还要推入起点的两个初始方向（向右和向下），
    # 这样循环逻辑才能统一处理“直走”和“转弯”。
    # 初始 steps 为 0，表示还没在那个方向移动过。
    pq = [
        (0, 0, 0, 0, 1, 0),  # 向右 (East)
        (0, 0, 0, 1, 0, 0)   # 向下 (South)
    ]
    
    # 记录已访问状态，避免死循环和重复计算
    # 状态 Key: (r, c, dr, dc, steps)
    seen = set()
    
    while pq:
        hl, r, c, dr, dc, steps = heapq.heappop(pq)
        
        # 到达终点检查
        if r == rows - 1 and c == cols - 1:
            # Part 2 特殊规则：必须至少连续走 min_steps 才能停止
            if steps >= min_steps:
                return hl
            # 如果步数不够，虽然到了终点但不能停，只能继续走（实际上通常意味着这条路废了，因为出界）
            # 但这里我们不能 return，要让它继续尝试（虽然很可能下一步就出界了）
        
        state_key = (r, c, dr, dc, steps)
        if state_key in seen:
            continue
        seen.add(state_key)
        
        # --- 尝试移动 ---
        # 我们可以做两件事：
        # 1. 保持当前方向直走 (如果 steps < max_steps)
        # 2. 向左或向右转 90度 (如果 steps >= min_steps)
        
        # 为了简化代码，我们尝试所有 4 个方向，然后根据规则过滤
        for ndr, ndc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # 规则 0: 禁止掉头 (不能往回走)
            if (ndr, ndc) == (-dr, -dc):
                continue
            
            # 判断是直走还是转弯
            if (ndr, ndc) == (dr, dc):
                # --- 直走情况 ---
                if steps < max_steps:
                    nr, nc = r + ndr, c + ndc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        new_hl = hl + grid[nr][nc]
                        heapq.heappush(pq, (new_hl, nr, nc, ndr, ndc, steps + 1))
            else:
                # --- 转弯情况 ---
                # 只有当前方向已经走了足够的步数 (min_steps) 才能转弯
                # (对于起点 steps=0 的情况，由于 min_steps 在 part2 是 4，
                #  0 < 4 所以不能转弯，只能直走，这符合逻辑)
                if steps >= min_steps:
                    nr, nc = r + ndr, c + ndc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        new_hl = hl + grid[nr][nc]
                        # 转弯后，新方向的计数重置为 1
                        heapq.heappush(pq, (new_hl, nr, nc, ndr, ndc, 1))

    return -1 # 应该不会发生

def solve():
    input_file = './input.txt'
    grid = parse_input(input_file)
    
    # Part 1: 最小 0 步(实际上转弯重置为1所以无所谓), 最大 3 步
    # 这里 min_steps 设为 0 或 1 效果一样，因为转弯后 steps 重置为 1，
    # 而只有 steps >= min 才能转弯。设为 0 允许刚走完一步就转弯。
    part1_result = solve_dijkstra(grid, min_steps=0, max_steps=3)
    print(f"[Part1] : {part1_result}")
    
    # Part 2: 最小 4 步, 最大 10 步
    part2_result = solve_dijkstra(grid, min_steps=4, max_steps=10)
    print(f"[Part2] : {part2_result}")

if __name__ == '__main__':
    solve()