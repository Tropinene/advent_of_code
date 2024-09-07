# 定义方向：上, 右, 下, 左
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 节点状态
CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3

# 解析输入，将感染节点记录到一个字典中，初始状态为清洁或感染
def parse_input(filename):
    grid = {}
    with open(filename) as f:
        lines = [line.strip() for line in f]
        size = len(lines)
        for r in range(size):
            for c in range(size):
                if lines[r][c] == '#':
                    grid[(r, c)] = INFECTED  # 初始感染节点
                else:
                    grid[(r, c)] = CLEAN  # 初始清洁节点
    return grid, size // 2  # 返回感染节点集合以及起始中心位置


# 进行病毒载体的模拟 - Part 1（没有进化）
def simulate_part1(grid, start_pos, bursts):
    x, y = start_pos, start_pos  # 载体从中间开始
    direction = 0  # 起始方向是向上
    infections_caused = 0

    for _ in range(bursts):
        if (x, y) in grid and grid[(x, y)] == INFECTED:
            # 当前节点被感染 -> 向右转，清除感染
            direction = (direction + 1) % 4
            grid[(x, y)] = CLEAN  # 清洁节点
        else:
            # 当前节点是清洁的 -> 向左转，感染该节点
            direction = (direction - 1) % 4
            grid[(x, y)] = INFECTED  # 感染节点
            infections_caused += 1

        # 前进到下一个节点
        x += directions[direction][0]
        y += directions[direction][1]

    return infections_caused


# 进行病毒载体的模拟 - Part 2（病毒进化）
def simulate_part2(grid, start_pos, bursts):
    x, y = start_pos, start_pos  # 载体从中间开始
    direction = 0  # 起始方向是向上
    infections_caused = 0

    for _ in range(bursts):
        current_state = grid.get((x, y), CLEAN)  # 获取当前节点状态，默认为清洁

        # 根据当前状态决定转向和状态变更
        if current_state == CLEAN:
            direction = (direction - 1) % 4  # 左转
            grid[(x, y)] = WEAKENED  # 节点变成弱化
        elif current_state == WEAKENED:
            # 不转向，节点变为感染
            grid[(x, y)] = INFECTED
            infections_caused += 1
        elif current_state == INFECTED:
            direction = (direction + 1) % 4  # 右转
            grid[(x, y)] = FLAGGED  # 节点变为标记
        elif current_state == FLAGGED:
            direction = (direction + 2) % 4  # 反向转身
            grid[(x, y)] = CLEAN  # 节点变为清洁

        # 前进到下一个节点
        x += directions[direction][0]
        y += directions[direction][1]

    return infections_caused


def main():
    # 读取输入并解析
    grid, start_pos = parse_input("input.txt")

    # 执行Part1病毒载体行为模拟
    result_part1 = simulate_part1(grid.copy(), start_pos, 10000)
    print(f"[Part1] : {result_part1}")

    # 执行Part2病毒进化后的行为模拟
    result_part2 = simulate_part2(grid.copy(), start_pos, 10000000)
    print(f"[Part2] : {result_part2}")


if __name__ == "__main__":
    main()
