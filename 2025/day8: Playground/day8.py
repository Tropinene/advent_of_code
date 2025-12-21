import math
from itertools import combinations

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) # 路径压缩
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # 按秩合并
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.num_sets -= 1
            return True
        return False

def solve_junction_boxes(data_str):
    # 1. 解析数据
    points = []
    for line in data_str.strip().split('\n'):
        if line.strip():
            points.append(tuple(map(int, line.split(','))))
    
    n = len(points)
    
    # 2. 计算所有边并排序 (Kruskal 算法基础)
    edges = []
    for i, j in combinations(range(n), 2):
        p1, p2 = points[i], points[j]
        # 使用平方距离避免浮点开方运算，提高速度
        dist_sq = sum((p1[k] - p2[k])**2 for k in range(3))
        edges.append((dist_sq, i, j))
    
    edges.sort()

    # --- 第一部分逻辑 ---
    uf_part1 = UnionFind(n)
    # 处理前 1000 个最短连接
    for k in range(min(1000, len(edges))):
        _, u, v = edges[k]
        uf_part1.union(u, v)
    
    # 获取所有电路的大小
    all_sizes = sorted([uf_part1.size[i] for i in range(n) if uf_part1.parent[i] == i], reverse=True)
    part1_result = 1
    for s in all_sizes[:3]:
        part1_result *= s

    print(f"[Part1] : {part1_result}")

    # --- 第二部分逻辑 ---
    uf_part2 = UnionFind(n)
    last_x_product = 0
    
    # 按距离从小到大遍历所有边，直到只剩一个集合
    for _, u, v in edges:
        if uf_part2.union(u, v):
            # 如果这次合并让所有点都连通了
            if uf_part2.num_sets == 1:
                last_x_product = points[u][0] * points[v][0]
                break
    
    print(f"[Part2] : {last_x_product}")


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_data = f.read()
    solve_junction_boxes(input_data)