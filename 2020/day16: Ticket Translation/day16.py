import re
import math

def solve():
    try:
        with open('./input.txt', 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print("错误: 未找到 ./input.txt 文件。")
        return

    # 输入分为三个部分
    blocks = content.split('\n\n')
    
    # 1. 解析规则 (Rules)
    # 格式: class: 1-3 or 5-7
    rules = {}
    rule_regex = re.compile(r'([^:]+): (\d+)-(\d+) or (\d+)-(\d+)')
    
    for line in blocks[0].split('\n'):
        match = rule_regex.match(line)
        if match:
            name = match.group(1)
            # 存储为两个范围元组: [(min1, max1), (min2, max2)]
            ranges = [
                (int(match.group(2)), int(match.group(3))),
                (int(match.group(4)), int(match.group(5)))
            ]
            rules[name] = ranges

    # 2. 解析我的票 (My Ticket)
    my_ticket_line = blocks[1].split('\n')[1]
    my_ticket = list(map(int, my_ticket_line.split(',')))

    # 3. 解析附近的票 (Nearby Tickets)
    nearby_tickets = []
    for line in blocks[2].split('\n')[1:]:
        nearby_tickets.append(list(map(int, line.split(','))))

    # --- Part 1: 扫描错误率并过滤无效票 ---
    
    scanning_error_rate = 0
    valid_tickets = []

    def is_value_valid_for_any_rule(val):
        """检查一个值是否至少符合所有的规则中的某一个"""
        for ranges in rules.values():
            r1, r2 = ranges
            if (r1[0] <= val <= r1[1]) or (r2[0] <= val <= r2[1]):
                return True
        return False

    for ticket in nearby_tickets:
        is_ticket_valid = True
        for val in ticket:
            if not is_value_valid_for_any_rule(val):
                scanning_error_rate += val
                is_ticket_valid = False
        
        # 只有每个数字都至少符合某一个规则，这张票才算有效
        if is_ticket_valid:
            valid_tickets.append(ticket)

    print(f"[Part1] : {scanning_error_rate}")

    # --- Part 2: 确定字段列 ---

    num_columns = len(my_ticket)
    
    # 初始化候选列表：假设每一列都可能是任意一个字段
    # col_candidates[i] 是第 i 列所有可能的字段名集合
    col_candidates = [set(rules.keys()) for _ in range(num_columns)]

    # 遍历所有有效票，进行排除
    for ticket in valid_tickets:
        for i, val in enumerate(ticket):
            # 检查当前列的值 val 是否违反了某个规则
            # 如果违反了，就从该列的候选集合中移除该规则名
            for name in list(col_candidates[i]): # 使用 list() 创建副本以在循环中修改集合
                r1, r2 = rules[name]
                if not ((r1[0] <= val <= r1[1]) or (r2[0] <= val <= r2[1])):
                    col_candidates[i].remove(name)

    # 约束传播：将候选集合收敛为唯一字段
    # 类似于 Day 21，如果你发现某一列只剩下一个可能的字段，那它就确定了
    # 然后需要从其他所有列的候选集合中把这个字段移除
    
    column_mapping = {} # 结果映射: {列索引: 字段名}
    
    while len(column_mapping) < num_columns:
        for i in range(num_columns):
            # 如果某列尚未确定，且候选只剩1个
            if i not in column_mapping and len(col_candidates[i]) == 1:
                field_name = list(col_candidates[i])[0]
                column_mapping[i] = field_name
                
                # 从其他所有列中移除这个字段
                for j in range(num_columns):
                    if j != i and field_name in col_candidates[j]:
                        col_candidates[j].remove(field_name)

    # 计算答案：所有以 'departure' 开头的字段对应在 'my_ticket' 中的值的乘积
    part2_ans = 1
    departure_fields = []
    
    for idx, name in column_mapping.items():
        if name.startswith('departure'):
            val = my_ticket[idx]
            part2_ans *= val
            departure_fields.append(f"{name}: {val}")

    print(f"[Part2] : {part2_ans}")

if __name__ == "__main__":
    solve()