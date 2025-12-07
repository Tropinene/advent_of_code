from collections import deque

def solve_part1(filename):
    """Part 1: Count how many times the beam is split"""
    with open(filename, 'r') as f:
        grid = [line.rstrip('\n') for line in f.readlines()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # 找到起始位置 S
    start_col = -1
    for col in range(cols):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    if start_col == -1:
        return 0
    
    # 使用队列来追踪所有活跃的束
    queue = deque([(1, start_col)])
    visited = set()
    visited.add((1, start_col))
    
    split_count = 0
    
    while queue:
        row, col = queue.popleft()
        
        # 检查是否越界
        if row >= rows or col < 0 or col >= cols:
            continue
        
        # 检查列是否在当前行的范围内
        if col >= len(grid[row]):
            continue
        
        current = grid[row][col]
        
        if current == '^':
            # 遇到分裂器，计数+1
            split_count += 1
            
            # 产生两束新的束：左边和右边
            left_col = col - 1
            right_col = col + 1
            
            # 左边的束
            if left_col >= 0 and row + 1 < rows and left_col < len(grid[row + 1]):
                if (row + 1, left_col) not in visited:
                    visited.add((row + 1, left_col))
                    queue.append((row + 1, left_col))
            
            # 右边的束
            if right_col < cols and row + 1 < rows and right_col < len(grid[row + 1]):
                if (row + 1, right_col) not in visited:
                    visited.add((row + 1, right_col))
                    queue.append((row + 1, right_col))
        
        elif current == '.':
            # 空白空间，束继续向下
            next_row = row + 1
            if next_row < rows and col < len(grid[next_row]):
                if (next_row, col) not in visited:
                    visited.add((next_row, col))
                    queue.append((next_row, col))
    
    return split_count


def solve_part2(filename):
    """Part 2: Count the number of different timelines (paths)"""
    with open(filename, 'r') as f:
        grid = [line.rstrip('\n') for line in f.readlines()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # 找到起始位置 S
    start_col = -1
    for col in range(cols):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    if start_col == -1:
        return 0
    
    # 使用动态规划：dp[row][col] = 到达该位置的路径数
    dp = {}
    dp[(1, start_col)] = 1  # 从S的下一行开始
    
    # 使用队列进行BFS，按行处理
    queue = deque([(1, start_col)])
    visited = set()
    visited.add((1, start_col))
    
    # 收集所有需要处理的位置
    positions = []
    while queue:
        row, col = queue.popleft()
        
        if row >= rows or col < 0 or col >= cols:
            continue
        
        if col >= len(grid[row]):
            continue
        
        positions.append((row, col))
        current = grid[row][col]
        
        if current == '^':
            # 分裂器：向左和向右
            left_col = col - 1
            right_col = col + 1
            
            if left_col >= 0 and row + 1 < rows and left_col < len(grid[row + 1]):
                if (row + 1, left_col) not in visited:
                    visited.add((row + 1, left_col))
                    queue.append((row + 1, left_col))
            
            if right_col < cols and row + 1 < rows and right_col < len(grid[row + 1]):
                if (row + 1, right_col) not in visited:
                    visited.add((row + 1, right_col))
                    queue.append((row + 1, right_col))
        
        elif current == '.':
            # 空白：继续向下
            next_row = row + 1
            if next_row < rows and col < len(grid[next_row]):
                if (next_row, col) not in visited:
                    visited.add((next_row, col))
                    queue.append((next_row, col))
    
    # 按行排序，从上到下计算路径数
    positions.sort()
    
    for row, col in positions:
        if (row, col) not in dp:
            dp[(row, col)] = 0
        
        current_paths = dp[(row, col)]
        
        if row >= rows or col >= len(grid[row]):
            continue
        
        current = grid[row][col]
        
        if current == '^':
            # 分裂：路径数分配给左右两个子节点
            left_col = col - 1
            right_col = col + 1
            
            if left_col >= 0 and row + 1 < rows and left_col < len(grid[row + 1]):
                if (row + 1, left_col) not in dp:
                    dp[(row + 1, left_col)] = 0
                dp[(row + 1, left_col)] += current_paths
            
            if right_col < cols and row + 1 < rows and right_col < len(grid[row + 1]):
                if (row + 1, right_col) not in dp:
                    dp[(row + 1, right_col)] = 0
                dp[(row + 1, right_col)] += current_paths
        
        elif current == '.':
            # 继续向下：路径数传递给下一个位置
            next_row = row + 1
            if next_row < rows and col < len(grid[next_row]):
                if (next_row, col) not in dp:
                    dp[(next_row, col)] = 0
                dp[(next_row, col)] += current_paths
    
    # 计算所有终点（没有后续节点的位置）的路径数总和
    terminal_positions = set()
    for row, col in positions:
        if row >= rows or col >= len(grid[row]):
            continue
        
        current = grid[row][col]
        has_next = False
        
        if current == '^':
            left_col = col - 1
            right_col = col + 1
            if (left_col >= 0 and row + 1 < rows and left_col < len(grid[row + 1])) or \
               (right_col < cols and row + 1 < rows and right_col < len(grid[row + 1])):
                has_next = True
        elif current == '.':
            next_row = row + 1
            if next_row < rows and col < len(grid[next_row]):
                has_next = True
        
        if not has_next:
            terminal_positions.add((row, col))
    
    total_timelines = sum(dp.get(pos, 0) for pos in terminal_positions)
    
    return total_timelines


# 主程序
if __name__ == "__main__":
    part1_result = solve_part1('input.txt')
    print(f"[Part1]: {part1_result}")
    
    part2_result = solve_part2('input.txt')
    print(f"[Part2]: {part2_result}")