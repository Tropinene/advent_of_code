import math
import sys

def read_input(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    return content.split('\n\n')

class Tile:
    def __init__(self, raw_data):
        lines = raw_data.strip().split('\n')
        self.id = int(lines[0].split()[1][:-1])
        self.grid = [list(line) for line in lines[1:]]
        self.size = len(self.grid)
        self.update_edges()

    def update_edges(self):
        # 提取四个边缘
        # top, right, bottom, left
        self.edges = [
            "".join(self.grid[0]),
            "".join([row[-1] for row in self.grid]),
            "".join(self.grid[-1]),
            "".join([row[0] for row in self.grid])
        ]
    
    def rotate(self):
        # 顺时针旋转90度
        self.grid = [list(row) for row in zip(*self.grid[::-1])]
        self.update_edges()

    def flip(self):
        # 水平翻转
        self.grid = [row[::-1] for row in self.grid]
        self.update_edges()

    def all_possible_borders(self):
        # 返回所有边缘及其翻转版本，用于Part 1快速匹配
        borders = set()
        for e in self.edges:
            borders.add(e)
            borders.add(e[::-1])
        return borders

    def remove_borders(self):
        # Part 2: 去除外围一圈
        new_grid = []
        for r in range(1, len(self.grid) - 1):
            new_grid.append(self.grid[r][1:-1])
        return new_grid

def get_shared_borders_count(tiles):
    # 计算每个Tile有多少个边缘能与其他Tile匹配
    border_map = {}
    for t in tiles:
        for b in t.all_possible_borders():
            if b not in border_map: border_map[b] = []
            border_map[b].append(t.id)
    
    tile_neighbors = {t.id: 0 for t in tiles}
    for b, ids in border_map.items():
        if len(ids) > 1: # 这是一个共享边缘
            for tid in ids:
                tile_neighbors[tid] += 1
    
    # 每个边被计算了两次（正向和反向），所以除以2
    # 角落Tile会有2个邻居（4个匹配边），边缘有3个，中间有4个
    return {tid: count // 2 for tid, count in tile_neighbors.items()}

def match_pattern(image, pattern):
    h, w = len(image), len(image[0])
    ph, pw = len(pattern), len(pattern[0])
    count = 0
    
    # 扫描整张大图
    for y in range(h - ph + 1):
        for x in range(w - pw + 1):
            match = True
            for dy in range(ph):
                for dx in range(pw):
                    if pattern[dy][dx] == '#' and image[y+dy][x+dx] != '#':
                        match = False
                        break
                if not match: break
            if match:
                count += 1
    return count

def solve():
    try:
        raw_tiles = read_input('./input.txt')
    except FileNotFoundError:
        print("错误: 未找到 ./input.txt 文件。")
        return

    tiles = [Tile(rt) for rt in raw_tiles]
    tile_map = {t.id: t for t in tiles}

    # --- Part 1 ---
    # 找出每个Tile有多少个匹配边
    neighbors_count = get_shared_borders_count(tiles)
    
    corners = [tid for tid, count in neighbors_count.items() if count == 2]
    part1_ans = math.prod(corners)
    
    print(f"--- Part 1 ---")
    print(f"角落 Tile IDs: {corners}")
    print(f"答案 (乘积): {part1_ans}")
    print("-" * 20)

    # --- Part 2 ---
    # 1. 拼图
    # 假设拼图是正方形
    grid_size = int(math.sqrt(len(tiles)))
    assembled = [[None for _ in range(grid_size)] for _ in range(grid_size)]
    used_ids = set()

    # 选取第一个角落作为左上角 (0,0)
    top_left_id = corners[0]
    top_left_tile = tile_map[top_left_id]
    used_ids.add(top_left_id)
    assembled[0][0] = top_left_tile

    # 我们需要找到所有Tiles之间的连接关系
    # 预计算所有边的拥有者，方便查找
    edge_lookup = {}
    for t in tiles:
        for e in t.all_possible_borders():
            if e not in edge_lookup: edge_lookup[e] = []
            edge_lookup[e].append(t)

    # 调整左上角方向：确保它的匹配边位于 右(idx 1) 和 下(idx 2)
    # 因为它是角落，只有2个邻居。我们旋转它直到它的 右边 和 下边 能在 edge_lookup 中找到邻居
    for _ in range(2):     # Flip
        for _ in range(4): # Rotate
            right_edge = top_left_tile.edges[1]
            bottom_edge = top_left_tile.edges[2]
            # 检查是否有邻居拥有这两个边 (排除自己)
            has_right = len([x for x in edge_lookup[right_edge] if x.id != top_left_tile.id]) > 0
            has_bottom = len([x for x in edge_lookup[bottom_edge] if x.id != top_left_tile.id]) > 0
            
            if has_right and has_bottom:
                break # 方向正确
            top_left_tile.rotate()
        else:
            top_left_tile.flip()
            continue
        break
    
    # 开始填充网格
    for r in range(grid_size):
        for c in range(grid_size):
            if r == 0 and c == 0: continue
            
            if c > 0:
                # 匹配左边Tile的右边缘
                target_edge = assembled[r][c-1].edges[1] # 左边邻居的Right edge
                candidates = [t for t in edge_lookup[target_edge] if t.id not in used_ids]
                edge_idx_to_match = 3 # 当前Tile的Left edge (idx 3) 需要匹配 target
            else:
                # 匹配上边Tile的下边缘
                target_edge = assembled[r-1][c].edges[2] # 上边邻居的Bottom edge
                candidates = [t for t in edge_lookup[target_edge] if t.id not in used_ids]
                edge_idx_to_match = 0 # 当前Tile的Top edge (idx 0) 需要匹配 target
            
            if not candidates:
                print(f"Error: No match found for pos {r},{c}")
                return

            current_tile = candidates[0]
            
            # 旋转/翻转当前Tile以匹配边缘
            found_orientation = False
            for _ in range(2):
                for _ in range(4):
                    if current_tile.edges[edge_idx_to_match] == target_edge:
                        found_orientation = True
                        break
                    current_tile.rotate()
                if found_orientation: break
                current_tile.flip()
            
            assembled[r][c] = current_tile
            used_ids.add(current_tile.id)

    # 2. 合并图像 (去除边框)
    final_image = []
    tile_h = len(assembled[0][0].grid) - 2
    
    for r in range(grid_size):
        for row_idx in range(tile_h):
            full_row = ""
            for c in range(grid_size):
                # 获取去边框后的行
                cleaned_grid = assembled[r][c].remove_borders()
                full_row += "".join(cleaned_grid[row_idx])
            final_image.append(list(full_row))

    # 3. 寻找海怪
    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]
    
    # 计算海怪里的 # 数量
    monster_hashes = sum(row.count('#') for row in monster)
    total_hashes = sum(row.count('#') for row in final_image)
    
    # 尝试所有8种方向寻找海怪
    monsters_found = 0
    
    # 定义简单的网格操作函数用于最终大图
    def rotate_grid(g): return [list(r) for r in zip(*g[::-1])]
    def flip_grid(g): return [r[::-1] for r in g]
    
    current_image = final_image
    for _ in range(2):
        for _ in range(4):
            count = match_pattern(current_image, monster)
            if count > 0:
                monsters_found = count
                break
            current_image = rotate_grid(current_image)
        if monsters_found > 0: break
        current_image = flip_grid(current_image)

    roughness = total_hashes - (monsters_found * monster_hashes)
    
    print(f"--- Part 2 ---")
    print(f"发现海怪数量: {monsters_found}")
    print(f"水的粗糙度 (答案): {roughness}")

if __name__ == '__main__':
    solve()