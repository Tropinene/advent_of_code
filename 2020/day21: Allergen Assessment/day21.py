import sys

def solve():
    try:
        with open('./input.txt', 'r') as f:
            lines = f.read().strip().split('\n')
    except FileNotFoundError:
        print("错误: 未找到 ./input.txt 文件。")
        return

    # 数据结构
    # allergen_candidates: 字典 { 'dairy': {'mxmxvkd', ...}, ... }
    # 用于存储每个过敏源可能对应的成分集合
    allergen_candidates = {}
    
    # all_ingredient_occurrences: 列表
    # 记录所有食品清单中出现的所有成分（不去重），用于Part 1计数
    all_ingredient_occurrences = []

    # 1. 解析输入并缩小候选范围
    for line in lines:
        # 格式示例: "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)"
        if ' (contains ' in line:
            parts = line.split(' (contains ')
            ingredients_str = parts[0]
            allergens_str = parts[1][:-1] # 去掉右括号
            
            current_ingredients = set(ingredients_str.split())
            current_allergens = allergens_str.split(', ')
            
            # 将当前行的成分加入总列表
            all_ingredient_occurrences.extend(list(current_ingredients))

            for alg in current_allergens:
                if alg not in allergen_candidates:
                    # 第一次遇到该过敏源，初始化为当前行的所有成分
                    allergen_candidates[alg] = current_ingredients.copy()
                else:
                    # 再次遇到该过敏源，取交集
                    # 因为该过敏源必须存在于所有包含它的食品行中
                    allergen_candidates[alg] &= current_ingredients

    # --- Part 1 ---
    
    # 找出所有可能的过敏源成分（即所有候选集合的并集）
    possible_allergenic_ingredients = set()
    for ingredients in allergen_candidates.values():
        possible_allergenic_ingredients.update(ingredients)

    # 统计“安全”成分出现的次数
    # 安全成分 = 总成分 - 可能含有过敏源的成分
    safe_count = 0
    for ing in all_ingredient_occurrences:
        if ing not in possible_allergenic_ingredients:
            safe_count += 1

    print(f"[Part1] : {safe_count}")


    # --- Part 2 ---
    
    # 此时 allergen_candidates 可能看起来像:
    # {'dairy': {'mxmxvkd'}, 'fish': {'mxmxvkd', 'sqjhc'}}
    # 我们需要推导出唯一的一对一映射。
    
    final_mapping = {} # { 'dairy': 'mxmxvkd', ... }
    
    # 只要还有过敏源没确定，就继续循环
    while len(final_mapping) < len(allergen_candidates):
        found_fixed = False
        
        for alg, candidates in allergen_candidates.items():
            # 如果某个过敏源只剩下一个候选成分，那它就是唯一解
            if alg not in final_mapping and len(candidates) == 1:
                confirmed_ingredient = list(candidates)[0]
                final_mapping[alg] = confirmed_ingredient
                found_fixed = True
                
                # 从其他所有过敏源的候选列表中移除这个已确定的成分
                for other_alg in allergen_candidates:
                    if other_alg != alg and confirmed_ingredient in allergen_candidates[other_alg]:
                        allergen_candidates[other_alg].remove(confirmed_ingredient)
                break
        
        if not found_fixed:
            # 理论上根据题目保证，不会进入死循环
            break

    # 题目要求：按过敏源的英语单词字母顺序排序
    sorted_allergens = sorted(final_mapping.keys())
    
    # 获取对应的成分列表
    dangerous_ingredients = [final_mapping[alg] for alg in sorted_allergens]
    
    # 用逗号连接
    part2_ans = ",".join(dangerous_ingredients)

    print(f"[Part2] : {part2_ans}")

if __name__ == "__main__":
    solve()