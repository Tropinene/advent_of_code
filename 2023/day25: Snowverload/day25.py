import networkx as nx
import sys

def solve():
    # 创建一个无向图
    G = nx.Graph()

    # 读取输入文件
    input_path = './input.txt'
    try:
        with open(input_path, 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                # 解析每一行，格式如 "jqt: rhn xhk nvd"
                node, neighbors_str = line.strip().split(': ')
                neighbors = neighbors_str.split()
                for neighbor in neighbors:
                    # 添加边 (会自动处理重复和无向性质)
                    G.add_edge(node, neighbor)
    except FileNotFoundError:
        print(f"错误: 找不到文件 {input_path}")
        return

    # 使用 Stoer-Wagner 算法寻找全局最小割
    # 该算法返回 (cut_value, (partition1, partition2))
    try:
        cut_value, partition = nx.stoer_wagner(G)
    except Exception as e:
        print(f"算法执行出错: {e}")
        return

    if cut_value == 3:
        group1_size = len(partition[0])
        group2_size = len(partition[1])
        result = group1_size * group2_size
        
        print(f"[Part1] : {result}")

if __name__ == '__main__':
    solve()