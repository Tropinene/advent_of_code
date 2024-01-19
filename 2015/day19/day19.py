import random

def findall(text, sub):
    position = []
    idx = text.find(sub)
    while idx != -1:
        position.append(idx)
        idx = text.find(sub, idx + 1)
    return position

def find_min_steps_to_molecule(target_molecule, dic):
    steps = 0
    current_molecule = target_molecule

    # 逆向替换，从目标分子逆推到 'e'
    while current_molecule != 'e':
        # 修复：随机选择替换规则
        replace, old = random.choice(list(dic.items()))
        if replace in current_molecule:
            current_molecule = current_molecule.replace(replace, old, 1)  # 逆向替换一次
            steps += 1

    return steps


if __name__ == '__main__':
    lines = open('./input.txt', 'r').readlines()
    s = lines[-1].strip()
    dic = {}
    res = set()

    for line in lines[:-2]:
        old, replace = line.strip().split(' => ')
        if dic.get(old) is None:
            dic[old] = []
        dic[old].append(replace)

    for item, replacements in dic.items():
        for p in findall(s, item):
            for replace in replacements:
                new_s = s[:p] + replace + s[p + len(item):]
                res.add(new_s)

    print(f"[Part1] : {len(res)}")

    lines = open('./input.txt', 'r').readlines()
    target_molecule = lines[-1].strip()
    dic = {}

    # 构建逆向替换字典
    for line in lines[:-2]:
        old, replace = line.strip().split(' => ')
        dic[replace] = old

    min_steps = find_min_steps_to_molecule(target_molecule, dic)
    print(f"[Part2] : {min_steps}")