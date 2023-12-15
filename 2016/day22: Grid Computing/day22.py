# give disk nodes info
# part1: find the number of available node to store another node's information.

import re

if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    node_infos = data[2:]

    nodes = {}
    for node in node_infos:
        tmp_dict = {}
        lst = node.strip().split()
        node_name = lst[0].split('/')[-1]
        matches = re.findall(r'\d+', node_name)

        tmp_dict["location"] = (int(matches[0]), int(matches[1]))
        tmp_dict["size"], tmp_dict["used"], tmp_dict["avail"] = int(lst[1][:-1]), int(lst[2][:-1]), int(lst[3][:-1])
        nodes[node_name] = tmp_dict

    p1 = 0
    for node1 in nodes.keys():
        for node2 in nodes.keys():
            if node1 == node2:
                continue
            if nodes[node1]["used"] != 0 and nodes[node1]["used"] < nodes[node2]["avail"]:
                p1 += 1
    print(f"[Part1] : {p1}")
