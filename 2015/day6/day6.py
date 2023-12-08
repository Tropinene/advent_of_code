import re


def getData(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


if __name__ == "__main__":
    file_path = './input.txt'
    lines = getData(file_path)

    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    lights2 = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        coordinates = re.findall(r'\d+', line)
        if line.startswith('turn on'):
            for i in range(int(coordinates[0]), int(coordinates[2])+1):
                for j in range(int(coordinates[1]), int(coordinates[3])+1):
                    lights[i][j] = 1
                    lights2[i][j] += 1
        elif line.startswith('turn off'):
            for i in range(int(coordinates[0]), int(coordinates[2])+1):
                for j in range(int(coordinates[1]), int(coordinates[3])+1):
                    lights[i][j] = 0
                    lights2[i][j] -= 1
                    if lights2[i][j] < 0:
                        lights2[i][j] = 0
        elif line.startswith('toggle'):
            for i in range(int(coordinates[0]), int(coordinates[2])+1):
                for j in range(int(coordinates[1]), int(coordinates[3])+1):
                    lights[i][j] = (lights[i][j] + 1) % 2
                    lights2[i][j] += 2
    print(f'[Part1] : {sum(row_sum for row in lights for row_sum in row)}')
    print(f'[Part2] : {sum(row_sum for row in lights2 for row_sum in row)}')
