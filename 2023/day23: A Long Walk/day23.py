import sys

# 增加递归深度，以防万一
sys.setrecursionlimit(10000)

def solve():
    input_file = "./input.txt"
    try:
        with open(input_file, "r") as f:
            grid = f.read().splitlines()
    except FileNotFoundError:
        print(f"错误: 未找到 {input_file} 文件。")
        return

    rows = len(grid)
    cols = len(grid[0])
    
    start_pos = (0, grid[0].index('.'))
    end_pos = (rows - 1, grid[rows - 1].index('.'))

    # --- 辅助函数 ---

    def get_neighbors(r, c, is_part2):
        """获取 (r, c) 的有效邻居"""
        char = grid[r][c]
        dirs = []
        
        # Part 1: 必须遵守滑坡方向
        if not is_part2 and char in "^>v<":
            if char == '^': dirs = [(-1, 0)]
            elif char == 'v': dirs = [(1, 0)]
            elif char == '<': dirs = [(0, -1)]
            elif char == '>': dirs = [(0, 1)]
        else:
            # Part 2 或普通点: 四个方向
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                yield nr, nc

    def build_compressed_graph(is_part2):
        """
        将网格压缩成节点和带权重的边。
        节点 = 起点 + 终点 + 岔路口
        """
        # 1. 找出所有的关键节点 (Junctions)
        junctions = [start_pos, end_pos]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '#': continue
                # 如果一个点有 3 个或以上的邻居，它就是一个岔路口
                # 注意：这里判断邻居时只看是不是墙，不看滑坡方向（那是边的属性）
                neighbors_count = 0
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                        neighbors_count += 1
                if neighbors_count > 2:
                    junctions.append((r, c))
        
        # 使用集合加速查找
        junction_set = set(junctions)
        
        # 2. 构建邻接表: graph[u] = [(v, distance), ...]
        adj = {u: [] for u in junctions}

        for j_start in junctions:
            # 从每个岔路口出发进行 BFS/DFS，直到遇到另一个岔路口
            stack = [(j_start, 0)]
            visited = {j_start}
            
            while stack:
                (curr_r, curr_c), dist = stack.pop()
                
                # 如果走了一段距离后遇到了另一个岔路口
                if dist > 0 and (curr_r, curr_c) in junction_set:
                    adj[j_start].append(((curr_r, curr_c), dist))
                    continue # 这一条路结束，不用继续往下走了
                
                for nr, nc in get_neighbors(curr_r, curr_c, is_part2):
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append(((nr, nc), dist + 1))
        
        return adj

    # 全局变量用于存储最大路径
    max_path_length = 0

    def dfs_longest_path(current_node, target, visited, current_dist, graph):
        nonlocal max_path_length
        
        if current_node == target:
            if current_dist > max_path_length:
                max_path_length = current_dist
            return

        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs_longest_path(neighbor, target, visited, current_dist + weight, graph)
                visited.remove(neighbor) # 回溯

    # --- 执行 Part 1 ---
    graph_p1 = build_compressed_graph(is_part2=False)
    max_path_length = 0
    dfs_longest_path(start_pos, end_pos, {start_pos}, 0, graph_p1)
    print(f"[Part1] : {max_path_length}")

    # --- 执行 Part 2 ---
    graph_p2 = build_compressed_graph(is_part2=True)
    max_path_length = 0
    dfs_longest_path(start_pos, end_pos, {start_pos}, 0, graph_p2)
    print(f"[Part2] : {max_path_length}")

if __name__ == "__main__":
    solve()