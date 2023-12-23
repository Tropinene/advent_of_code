import re


def draw_matrix(rects, is_part2):
    matrix = [[0] * 1000 for _ in range(1000)]

    for r in rects:
        matches = re.findall(r'\d+', r.strip())
        matches = [int(x) for x in matches]
        idx, col, row, c_len, r_len = matches
        for i in range(r_len):
            for j in range(c_len):
                if not is_part2:
                    matrix[row + i][col + j] += 1
                else:
                    if matrix[row + i][col + j] != 0:
                        matrix[row + i][col + j] = '-1'
                    else:
                        matrix[row + i][col + j] = idx
    return matrix


if __name__ == '__main__':
    rects = open('input.txt', 'r').readlines()

    matrix = draw_matrix(rects, False)
    p1 = 0
    for i in range(1000):
        for j in range(1000):
            if matrix[i][j] > 1:
                p1 += 1
    print(f"[Part1] : {p1}")

    matrix = draw_matrix(rects, True)
    for r in rects:
        flag = True
        matches = re.findall(r'\d+', r.strip())
        matches = [int(x) for x in matches]
        idx, col, row, c_len, r_len = matches
        for i in range(r_len):
            for j in range(c_len):
                if matrix[row + i][col + j] != idx:
                    flag = False
        if flag:
            print(f"[Part2] : {idx}")
            break
