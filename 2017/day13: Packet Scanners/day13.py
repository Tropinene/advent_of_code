if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    dic = {}
    for line in data:
        name, depth = line.strip().split(': ')
        dic[int(name)] = int(depth)

    p1 = 0
    for i in dic.keys():
        if i % (2 * dic[i] - 2) == 0:
            p1 += i * dic[i]
    print(f"[Part1] : {p1}")

    delay = 1
    while True:
        is_caught = False
        for i in dic.keys():
            if (i + delay) % (2 * dic[i] - 2) == 0:
                is_caught = True
                break
        if not is_caught:
            break
        delay += 1
    print(f"[Part2] : {delay}")
