import numpy as np

def solve1(positions: list[list[int]]) -> int:
    res = 0
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i == j:
                continue
            l = positions[i][1] - positions[j][1] + 1
            w = positions[i][0] - positions[j][0] + 1
            res = max(res, l * w)
    return res

def solve2(positions: list[list[int]]) -> int:
    n = len(positions)
    xs = sorted(list(set(p[0] for p in positions)))
    ys = sorted(list(set(p[1] for p in positions)))
    
    # 坐标映射 (坐标压缩)
    x_map = {x: i for i, x in enumerate(xs)}
    y_map = {y: i for i, y in enumerate(ys)}
    
    # 构建压缩后的网格
    grid_w, grid_h = len(xs), len(ys)
    # filled[i][j] 表示 压缩坐标 (xs[i], ys[j]) 这个格子是否在多边形内
    filled = [[False] * grid_h for _ in range(grid_w)]

    # 1. 标记边缘
    edges = []
    for i in range(n):
        p1, p2 = positions[i], positions[(i + 1) % n]
        if p1[0] == p2[0]: # 垂直边
            x = p1[0]
            y_start, y_end = min(p1[1], p2[1]), max(p1[1], p2[1])
            edges.append((x, y_start, y_end))

    # 2. 填充内部 (扫描线逻辑)
    for j in range(len(ys)):
        y_val = ys[j]
        # 找到所有跨越当前 y 层的垂直边
        active_xs = []
        for x, y1, y2 in edges:
            if y1 <= y_val < y2:
                active_xs.append(x)
        active_xs.sort()
        
        # 填充奇偶区间
        for k in range(0, len(active_xs), 2):
            x_start, x_end = active_xs[k], active_xs[k+1]
            for i in range(x_map[x_start], x_map[x_end] + 1):
                filled[i][j] = True
    
    # 最后一行（多边形底边）需要单独处理或补齐
    # 由于是离散格子，我们让 filled[i][j] 代表点 (xs[i], ys[j])
    
    # 3. 二维前缀和 (基于压缩后的网格)
    pref = [[0] * (grid_h + 1) for _ in range(grid_w + 1)]
    for i in range(grid_w):
        for j in range(grid_h):
            val = 1 if filled[i][j] else 0
            pref[i+1][j+1] = val + pref[i][j+1] + pref[i+1][j] - pref[i][j]

    def is_all_filled(x1, y1, x2, y2):
        # 映射回压缩索引
        ix1, ix2 = sorted([x_map[x1], x_map[x2]])
        iy1, iy2 = sorted([y_map[y1], y_map[y2]])
        
        expected = (ix2 - ix1 + 1) * (iy2 - iy1 + 1)
        actual = pref[ix2+1][iy2+1] - pref[ix1][iy2+1] - pref[ix2+1][iy1] + pref[ix1][iy1]
        return expected == actual

    # 4. 遍历红点对 (加入更强的剪枝)
    res = 0
    # 按面积潜力降序排序点对可以更快剪枝，但这里直接遍历
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = positions[i], positions[j]
            area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            if area <= res:
                continue
            
            if is_all_filled(p1[0], p1[1], p2[0], p2[1]):
                res = area
                
    return res

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    positions = []
    for line in lines:
        positions.append(list(map(int, line.strip().split(","))))

    print(f"[Part1] : {solve1(positions)}")
    print(f"[Part2] : {solve2(positions)}")