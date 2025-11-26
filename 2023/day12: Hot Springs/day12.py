import functools

# 使用记忆化装饰器缓存函数结果，解决 Part 2 的性能问题
@functools.cache
def count_arrangements(pattern, counts):
    """
    递归计算符合 counts 要求的 pattern 排列方式数量。
    pattern: 当前剩余的弹簧字符串 (例如 "???.###")
    counts: 当前剩余的损坏弹簧组长度元组 (例如 (1, 1, 3))
    """
    
    # --- 基本情况 (Base Cases) ---
    
    # 如果没有剩余的组需要匹配
    if not counts:
        # 如果 pattern 中还有损坏的弹簧 '#', 说明这种排列无效（多了 '#'）
        # 否则有效（剩下的都是 '.' 或 '?' 当作 '.'）
        return 0 if "#" in pattern else 1
    
    # 如果没有剩余的 pattern 字符，但还有 counts 需要匹配，则无效
    if not pattern:
        return 0

    result = 0
    current_char = pattern[0]
    next_group_size = counts[0]

    # --- 逻辑分支 ---

    # 1. 尝试将当前字符视为 '.' (操作正常)
    # 如果当前字符是 '.' 或者 '?' (我们可以选择把它变成 '.')
    if current_char in ".?":
        result += count_arrangements(pattern[1:], counts)

    # 2. 尝试将当前字符视为 '#' (损坏)
    # 如果当前字符是 '#' 或者 '?' (我们可以选择把它变成 '#')
    if current_char in "#?":
        # 检查是否可以放置当前组 (长度为 next_group_size)
        # 条件 A: pattern 剩余长度必须足够
        # 条件 B: 接下来的 next_group_size 个字符中不能有 '.' (因为我们要放的是连续的 '#')
        # 条件 C: 这一组放完后，紧接着的字符不能是 '#' (必须有分隔符 '.' 或结束)
        if (len(pattern) >= next_group_size and 
            "." not in pattern[:next_group_size] and 
            (len(pattern) == next_group_size or pattern[next_group_size] != "#")):
            
            # 如果满足条件，我们消耗掉这一组 counts
            # 并跳过 pattern 中的 (组长度 + 1) 个字符
            # +1 是因为组与组之间至少要有一个分隔符 '.' (或者 pattern 结束)
            result += count_arrangements(pattern[next_group_size + 1:], counts[1:])

    return result

def solve():
    try:
        with open("./input.txt", "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print("错误: 未找到 ./input.txt 文件。")
        return

    total_part1 = 0
    total_part2 = 0

    for line in lines:
        if not line.strip():
            continue
            
        parts = line.split()
        pattern = parts[0]
        # 将数字字符串转换为整数元组，例如 "1,1,3" -> (1, 1, 3)
        counts = tuple(map(int, parts[1].split(",")))

        # --- Part 1 ---
        total_part1 += count_arrangements(pattern, counts)
        

        # --- Part 2 ---
        # 展开规则：pattern 重复 5 次用 '?' 连接，counts 重复 5 次
        unfolded_pattern = "?".join([pattern] * 5)
        unfolded_counts = counts * 5
        
        total_part2 += count_arrangements(unfolded_pattern, unfolded_counts)
    
    print(f"[Part1] : {total_part1}")
    print(f"[Part2] : {total_part2}")

if __name__ == "__main__":
    solve()