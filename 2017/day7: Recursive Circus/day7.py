def count_weight(structure, weight, node):
    res = weight[node]
    if structure.get(node):
        lst = structure[node]
        for i in lst:
            res += count_weight(structure, weight, i)
    return res


def find_unique_number(dic):
    all_keys = list(dic.keys())
    if dic[all_keys[0]] == dic[all_keys[1]] == dic[all_keys[2]]:
        return None
    res = dic[all_keys[0]] ^ dic[all_keys[1]] ^ dic[all_keys[2]]
    for i in all_keys:
        if dic[i] == res:
            return i
    return None


if __name__ == "__main__":
    data = open('input.txt', 'r').readlines()

    structure, weight = {}, {}
    all_nodes = []
    for line in data:
        if '->' in line:
            tmp1, tmp2 = line.strip().split('->')
            parent, w = tmp1.split()
            weight[parent] = int(w.strip()[1:-1])
            sons = tmp2.split(',')
            sons = [x.strip() for x in sons]
            structure[parent] = sons
            all_nodes.extend(sons)
        else:
            name, w = line.split()
            all_nodes.append(name)
            weight[name] = int(w.strip()[1:-1])

    for parent in structure.keys():
        if parent not in all_nodes:
            print(f"[Part1] : {parent}")
            break

    subTree = structure[parent]
    last_parent = parent
    orgin_weight, gap = -1, -1
    while True:
        next_structure, next_parent = {}, None
        for node in subTree:
            w = count_weight(structure, weight, node)
            if orgin_weight == -1:
                orgin_weight = w
            if gap == -1 and w != orgin_weight:
                gap = abs(w - orgin_weight)
            next_structure[node] = w
        next_parent = find_unique_number(next_structure)
        if next_parent is None:
            print(f"[Part2] : {weight[last_parent]-gap}")
            break
        subTree = structure[next_parent]
        last_parent = next_parent
