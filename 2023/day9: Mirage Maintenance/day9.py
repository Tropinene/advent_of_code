def getData(file):
    with open(file, 'r') as f:
        data = f.readlines()
        f.close()
    return data


def find(lst, opt):
        differences = [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]

        common_difference = all(diff == differences[0] for diff in differences)

        if common_difference:
            if opt:
                return lst[-1] + differences[0]
            else:
                return lst[0] - differences[0]
        else:
            if opt:
                return lst[-1] + find(differences, 1)
            else:
                return lst[0] - find(differences, 0)


if __name__ == '__main__':
    file_path = './input.txt'
    data = getData(file_path)

    p1, p2 = 0, 0
    for line in data:
        lst = line.strip().split()
        lst = [int(x) for x in lst]
        p1 += find(lst, 1)
        p2 += find(lst, 0)

    print(f'[Part1] : {p1}')
    print(f'[Part2] : {p2}')