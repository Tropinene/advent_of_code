import os

def parse_input(filename):
    """读取文件并将每个图案块分割成行列表"""
    with open(filename, 'r') as f:
        content = f.read().strip()
    # 根据双换行符分割不同的图案
    patterns = [block.split('\n') for block in content.split('\n\n')]
    return patterns

def transpose(pattern):
    """转置网格：行变列，列变行"""
    # 使用 zip(*pattern) 进行转置，并将结果重新组合成字符串列表
    return [''.join(chars) for chars in zip(*pattern)]

def count_differences(line1, line2):
    """计算两个字符串之间不同字符的数量"""
    return sum(1 for a, b in zip(line1, line2) if a != b)

def find_reflection_score(pattern, target_diffs):
    """
    寻找满足特定差异数（target_diffs）的反射线。
    
    返回:
    - 0: 如果没有找到
    - n: 如果在第 n 行之后找到水平反射
    """
    rows = len(pattern)
    
    # 尝试在第 r 行之后切分 (r 从 1 到 rows-1)
    for r in range(1, rows):
        above = pattern[:r][::-1] # 切分线上面部分，翻转以便从切分线向外对比
        below = pattern[r:]       # 切分线下面部分
        
        # 只需要比较重叠部分的长度
        check_len = min(len(above), len(below))
        
        current_diffs = 0
        for i in range(check_len):
            current_diffs += count_differences(above[i], below[i])
            # 如果差异已经超过目标，提前停止（优化）
            if current_diffs > target_diffs:
                break
        
        # 如果整块区域对比完，差异恰好等于目标值，则找到了线
        if current_diffs == target_diffs:
            return r
            
    return 0

def solve():
    input_file = './input.txt'
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    patterns = parse_input(input_file)
    
    total_part1 = 0
    total_part2 = 0

    for pattern in patterns:
        # --- Part 1: 寻找完美反射 (差异为 0) ---
        
        # 1. 检查水平反射 (行) -> 得分 = 100 * 行数
        h_score_p1 = find_reflection_score(pattern, target_diffs=0)
        
        # 2. 检查垂直反射 (列) -> 转置后检查水平 -> 得分 = 列数
        v_score_p1 = find_reflection_score(transpose(pattern), target_diffs=0)
        
        total_part1 += (h_score_p1 * 100) + v_score_p1

        # --- Part 2: 寻找带污迹的反射 (差异为 1) ---
        
        h_score_p2 = find_reflection_score(pattern, target_diffs=1)
        v_score_p2 = find_reflection_score(transpose(pattern), target_diffs=1)
        
        total_part2 += (h_score_p2 * 100) + v_score_p2

    print(f"[Part1] : {total_part1}")
    print(f"[Part2] : {total_part2}")

if __name__ == '__main__':
    solve()