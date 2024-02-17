import heapq


def min_path_sum(matrix):
    paths = [(0, 0, 0)]
    rows, cols = len(matrix), len(matrix[0])

    visited = [[0] * cols for _ in range(rows)]

    while paths:
        total_cost, x, y = heapq.heappop(paths)

        if visited[x][y]:
            continue

        if (x, y) == (rows - 1, cols - 1):
            return total_cost

        visited[x][y] = 1
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                heapq.heappush(paths, (total_cost + matrix[nx][ny], nx, ny))


def parse_file():
    matrix = []
    with open('input.txt', 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip()]  # strip()用于删除行末尾的换行符
            matrix.append(row)
    return matrix


def enlarge_matrix(matrix):
    new_matrix = [[0] * len(row) * 5 for row in matrix * 5]
    r, c = len(matrix), len(matrix[0])

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            val = matrix[i % r][j % c] + i // r + j // c
            val = (val - 1) % 9 + 1
            new_matrix[i][j] = val
    return new_matrix


def main():
    matrix = parse_file()

    result = min_path_sum(matrix)
    print(f"[Part1] : {result}")

    matrix = enlarge_matrix(matrix)
    result = min_path_sum(matrix)
    print(f"[Part2] : {result}")


if __name__ == '__main__':
    main()

