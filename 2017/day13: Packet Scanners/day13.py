if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    dic = {}
    for line in data:
        name, depth = line.strip().split(': ')
        dic[int(name)] = int(depth)

    severity = 0
    for i in dic.keys():
        pass
