import sys
from fractions import Fraction

def solve():
    input_file = "./input.txt"
    try:
        with open(input_file, "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(f"错误: 未找到 {input_file} 文件。")
        return

    hailstones = []
    for line in lines:
        if not line.strip(): continue
        pos_str, vel_str = line.split('@')
        px, py, pz = map(int, pos_str.split(','))
        vx, vy, vz = map(int, vel_str.split(','))
        hailstones.append(((px, py, pz), (vx, vy, vz)))

    # --- Part 1: 2D 碰撞检测 (保持不变) ---
    TEST_MIN = 200000000000000
    TEST_MAX = 400000000000000
    total_part1 = 0
    
    for i in range(len(hailstones)):
        for j in range(i + 1, len(hailstones)):
            (px1, py1, _), (vx1, vy1, _) = hailstones[i]
            (px2, py2, _), (vx2, vy2, _) = hailstones[j]
            
            det = vx1 * (-vy2) - vy1 * (-vx2)
            if det == 0: continue
            
            t1 = ((px2 - px1) * (-vy2) - (py2 - py1) * (-vx2)) / det
            t2 = (vx1 * (py2 - py1) - vy1 * (px2 - px1)) / det
            
            if t1 >= 0 and t2 >= 0:
                ix = px1 + t1 * vx1
                iy = py1 + t1 * vy1
                if TEST_MIN <= ix <= TEST_MAX and TEST_MIN <= iy <= TEST_MAX:
                    total_part1 += 1
    
    print(f"[Part1] : {total_part1}")

    # --- Part 2: 线性代数解法 (无 Z3) ---
    # 我们需要构建 Ax = B，其中 x 是 [px, py, pz, vx, vy, vz]
    # 我们使用前 3 个冰雹来构建方程组
    # h0 和 h1 产生 3 个方程 (X, Y, Z 分量)
    # h0 和 h2 产生 3 个方程
    # 共 6 个方程，解 6 个未知数
    
    matrix = [] # 存储增广矩阵的行
    
    h0 = hailstones[0]
    (p0x, p0y, p0z), (v0x, v0y, v0z) = h0
    
    # 我们对比 h0 与 h1, 以及 h0 与 h2
    for target_h in [hailstones[1], hailstones[2]]:
        (pix, piy, piz), (vix, viy, viz) = target_h
        
        # 这里的推导基于 (P - Pi) x (V - Vi) = 0 的展开与消元
        # 未知数顺序: Px, Py, Pz, Vx, Vy, Vz
        
        # 1. 基于 X 分量的方程 (实际上来源于 Y, Z 的交叉项)
        # 对应的线性方程: (vy0 - vyi)Pz + (vzi - vz0)Py + (pz0 - pzi)Vy + (piy - p0y)Vz = ...
        row_x = [
            Fraction(0),                 # Px 系数
            Fraction(v0z - viz),         # Py 系数
            Fraction(viy - v0y),         # Pz 系数
            Fraction(0),                 # Vx 系数
            Fraction(piz - p0z),         # Vy 系数
            Fraction(p0y - piy),         # Vz 系数
            # 常数项 (移动到等号右边):
            Fraction(p0y * v0z - p0z * v0y - (piy * viz - piz * viy)) 
        ]
        matrix.append(row_x)

        # 2. 基于 Y 分量的方程
        row_y = [
            Fraction(viz - v0z),         # Px 系数
            Fraction(0),                 # Py 系数
            Fraction(v0x - vix),         # Pz 系数
            Fraction(p0z - piz),         # Vx 系数
            Fraction(0),                 # Vy 系数
            Fraction(pix - p0x),         # Vz 系数
            Fraction(p0z * v0x - p0x * v0z - (piz * vix - pix * viz))
        ]
        matrix.append(row_y)
        
        # 3. 基于 Z 分量的方程
        row_z = [
            Fraction(v0y - viy),         # Px 系数
            Fraction(vix - v0x),         # Py 系数
            Fraction(0),                 # Pz 系数
            Fraction(piy - p0y),         # Vx 系数
            Fraction(p0x - pix),         # Vy 系数
            Fraction(0),                 # Vz 系数
            Fraction(p0x * v0y - p0y * v0x - (pix * viy - piy * vix))
        ]
        matrix.append(row_z)

    # --- 高斯消元法求解 (Gaussian Elimination) ---
    # 矩阵大小应该为 6行 x 7列
    N = 6
    M = 7
    
    for i in range(N):
        # 1. 寻找主元 (Pivot)
        pivot_row = i
        for k in range(i + 1, N):
            if abs(matrix[k][i]) > abs(matrix[pivot_row][i]):
                pivot_row = k
        
        # 交换行
        matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
        
        # 2. 归一化主元行
        pivot = matrix[i][i]
        # 如果 pivot 为 0，说明有多重解或无解（这道题保证有唯一解）
        for j in range(i, M):
            matrix[i][j] /= pivot
            
        # 3. 消去其他行的该列
        for k in range(N):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, M):
                    matrix[k][j] -= factor * matrix[i][j]

    # 提取解
    # matrix[i][N] 是第 i 个未知数的值
    ans_px = matrix[0][6]
    ans_py = matrix[1][6]
    ans_pz = matrix[2][6]
    
    # 结果必须是整数，如果不是说明计算出错
    if ans_px.denominator == 1 and ans_py.denominator == 1 and ans_pz.denominator == 1:
        final_ans = int(ans_px) + int(ans_py) + int(ans_pz)
        print(f"[Part2] : {final_ans}")

if __name__ == "__main__":
    solve()