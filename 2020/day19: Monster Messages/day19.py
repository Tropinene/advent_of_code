import collections
import re

def parse_input(filename="./input.txt"):
    """
    读取输入文件，将规则解析成字典，并分离出消息列表。
    """
    with open(filename, 'r') as f:
        rules_raw, messages_raw = f.read().split('\n\n')

    rules = {}
    for line in rules_raw.splitlines():
        # 0: 4 1 5 或 1: 2 3 | 3 2 或 4: "a"
        num, rule_content = line.split(': ')
        num = int(num)

        if '"' in rule_content:
            # 基础规则，例如 4: "a"
            rules[num] = rule_content.strip().replace('"', '')
        else:
            # 复合规则，例如 1: 2 3 | 3 2
            alternatives = []
            for alt in rule_content.split(' | '):
                # 每个替代项是一系列规则编号
                alternatives.append([int(r) for r in alt.split()])
            rules[num] = alternatives
            
    messages = messages_raw.splitlines()
    return rules, messages

def match_rule(rules, message, rule_index, start_index):
    """
    递归匹配函数。
    尝试从 message 的 start_index 位置开始，匹配 rule_index 对应的规则。

    返回一个列表，包含所有成功的匹配结束后，在 message 中结束的索引位置。
    如果没有成功匹配，返回空列表。
    """
    
    # 如果起始索引超出消息长度，则不可能匹配
    if start_index >= len(message):
        return []

    rule = rules[rule_index]
    
    # 基础规则 (例如 "a" 或 "b")
    if isinstance(rule, str):
        if message.startswith(rule, start_index):
            # 匹配成功，返回匹配结束后的下一个索引位置
            return [start_index + len(rule)]
        else:
            return []

    # 复合规则 (例如 [[4, 1, 5], [4, 5]])
    successful_end_indices = []
    
    # 遍历所有 '或' 分支
    for sequence in rule:
        # 当前匹配序列从 start_index 开始
        current_indices = [start_index]
        
        # 遍历序列中的每个子规则
        for sub_rule_index in sequence:
            next_indices = []
            # 对于当前所有可能的结束位置，尝试匹配下一个子规则
            for current_end_index in current_indices:
                if current_end_index < len(message):
                    # 递归调用匹配下一个子规则
                    results = match_rule(rules, message, sub_rule_index, current_end_index)
                    next_indices.extend(results)
            
            # 如果没有匹配成功，此序列 (sequence) 匹配失败
            if not next_indices:
                current_indices = []
                break
            
            current_indices = next_indices
        
        # 如果此序列 (sequence) 成功匹配，将所有可能的结束索引加入结果列表
        successful_end_indices.extend(current_indices)
        
    return successful_end_indices


def solve_part1(rules, messages):
    """
    解决第一部分问题：计算有多少条消息完全匹配规则 0。
    """
    count = 0
    # 规则 0 总是只有一个序列，即 rules[0][0]
    # 我们调用 match_rule(rules, message, 0, 0)
    for message in messages:
        end_indices = match_rule(rules, message, 0, 0)
        # 只有当匹配结果中包含 message 的总长度时，才算是完全匹配
        if len(message) in end_indices:
            count += 1
    return count

def solve_part2(rules, messages):
    """
    解决第二部分问题：修改规则 8 和 11，然后重新计算。
    新规则:
    8: 42 | 42 8  (匹配一个或多个 42)
    11: 42 31 | 42 11 31 (匹配 N 个 42 后面跟着 N 个 31)
    """
    # 修改规则
    # 8: 42 | 42 8  => [[42], [42, 8]]
    rules[8] = [[42], [42, 8]]
    # 11: 42 31 | 42 11 31 => [[42, 31], [42, 11, 31]]
    rules[11] = [[42, 31], [42, 11, 31]]

    count = 0
    # 规则 0: 8 11
    # 这意味着我们必须匹配一个或多个 42 (规则 8)，后跟 N 个 42 和 N 个 31 (规则 11)。
    # 总结起来，消息必须匹配 (M+N) 个 42，然后是 N 个 31，其中 M >= 1, N >= 1。
    # 即：(42) * (M+N) + (31) * N，且 (M+N) > N >= 1
    # 简化：(42) * A + (31) * B，其中 A > B >= 1。
    
    # 然而，由于 match_rule 函数已经处理了递归，我们可以直接使用它：
    
    # 注意: 这个递归下降解析器在面对 Part 2 的深层递归时，
    # 可能会因为 Python 的默认递归限制而失败。
    # 更好的解决方案是使用专门的 Context-Free Grammar 匹配器或
    # 针对 A^N B^N 模式的特殊处理。
    
    # 对于本题，由于消息长度是有限的，我们可以将递归的规则 8 和 11 
    # 展开到足够覆盖最长消息的长度。
    
    # 但是，我们先尝试使用递归下降解析器：
    
    # 提升 Python 递归限制以应对 Part 2 的深递归
    import sys
    sys.setrecursionlimit(2000) 
    
    for message in messages:
        end_indices = match_rule(rules, message, 0, 0)
        if len(message) in end_indices:
            count += 1
            
    return count

def main():
    rules, messages = parse_input()
    
    # --- Part 1 ---
    # 由于 solve_part2 会修改 rules 字典，我们传递一个副本
    rules_part1 = collections.OrderedDict(rules) 
    result_part1 = solve_part1(rules_part1, messages)
    print(f"[Part1] : {result_part1}")

    # --- Part 2 ---
    rules_part2 = collections.OrderedDict(rules)
    result_part2 = solve_part2(rules_part2, messages)
    print(f"[Part2] : {result_part2}")

if __name__ == "__main__":
    main()