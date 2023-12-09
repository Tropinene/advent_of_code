import copy


def getData(path):
    lines = open(path, 'r').readlines()
    lines = [list(line.rstrip('\n')) for line in lines]
    return lines


if __name__ == '__main__':
    file_path = './input.txt'
    data = getData(file_path)

    rows = len(data)
    cols = len(data[0])
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for _ in range(100):
        matrix = copy.deepcopy(data)
        for i in range(rows):
            for j in range(cols):
                cnt = 0
                for dr, dc in neighbors:
                    r, c = i + dr, j + dc
                    if 0 <= r < rows and 0 <= c < cols:
                        cnt += 1 if data[r][c] == '#' else 0
                if data[i][j] == '#':
                    if cnt == 2 or cnt == 3:
                        matrix[i][j] = '#'
                    else:
                        matrix[i][j] = '.'
                else:
                    if cnt == 3:
                        matrix[i][j] = '#'
                    else:
                        matrix[i][j] = '.'
        data = copy.copy(matrix)

    p1 = 0
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == '#':
                p1 += 1
    print(f'[Part1] : {p1}')

    data = getData(file_path)
    for _ in range(100):
        matrix = copy.deepcopy(data)
        for i in range(rows):
            for j in range(cols):
                cnt = 0
                for dr, dc in neighbors:
                    r, c = i + dr, j + dc
                    if 0 <= r < rows and 0 <= c < cols:
                        cnt += 1 if data[r][c] == '#' else 0
                if data[i][j] == '#':
                    if cnt == 2 or cnt == 3:
                        matrix[i][j] = '#'
                    else:
                        matrix[i][j] = '.'
                else:
                    if cnt == 3:
                        matrix[i][j] = '#'
                    else:
                        matrix[i][j] = '.'
        matrix[0][0], matrix[0][cols-1], matrix[rows-1][0], matrix[rows-1][cols-1] = '#', '#', '#', '#'
        data = copy.copy(matrix)

    p2 = 0
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == '#':
                p2 += 1
    print(f'[Part2] : {p2}')
