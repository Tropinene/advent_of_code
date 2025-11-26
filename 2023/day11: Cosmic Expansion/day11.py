import sys

def solve():
    input_file = "./input.txt"
    try:
        with open(input_file, "r") as f:
            grid = f.read().splitlines()
    except FileNotFoundError:
        print(f"错误: 未找到 {input_file} 文件。")
        return

    if not grid:
        return

    rows = len(grid)
    cols = len(grid[0])

    # 1. 找出所有的空行和空列
    # 如果一行里没有 '#', 它就是空行
    empty_rows = {r for r, row in enumerate(grid) if '#' not in row}
    # 如果一列里全是 '.', 它就是空列
    empty_cols = {c for c in range(cols) if all(grid[r][c] == '.' for r in range(rows))}

    # 2. 找出所有星系的原始坐标
    galaxies = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                galaxies.append((r, c))

    # 3. 定义计算总距离的函数
    def calculate_total_distance(expansion_factor):
        # 预计算每一行/每一列对应的“真实”坐标值
        # 真实坐标 = 原始坐标 + (之前的空行数 * (膨胀系数 - 1))
        
        row_mapping = []
        expansion_offset = 0
        for r in range(rows):
            if r in empty_rows:
                # 减1是因为原本这一行占了1的空间，现在变成了 expansion_factor，所以增量是 factor-1
                expansion_offset += (expansion_factor - 1)
            row_mapping.append(r + expansion_offset)

        col_mapping = []
        expansion_offset = 0
        for c in range(cols):
            if c in empty_cols:
                expansion_offset += (expansion_factor - 1)
            col_mapping.append(c + expansion_offset)

        total_dist = 0
        # 计算所有星系对之间的距离
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                r1, c1 = galaxies[i]
                r2, c2 = galaxies[j]

                # 获取变换后的真实坐标
                real_r1, real_c1 = row_mapping[r1], col_mapping[c1]
                real_r2, real_c2 = row_mapping[r2], col_mapping[c2]

                # 曼哈顿距离
                dist = abs(real_r1 - real_r2) + abs(real_c1 - real_c2)
                total_dist += dist
        
        return total_dist
    
    # Part 1: 膨胀系数为 2 (变大一倍)
    part1_ans = calculate_total_distance(2)
    print(f"[Part1] : {part1_ans}")

    # Part 2: 膨胀系数为 1,000,000
    part2_ans = calculate_total_distance(1000000)
    print(f"[Part2] : {part2_ans}")

if __name__ == "__main__":
    solve()