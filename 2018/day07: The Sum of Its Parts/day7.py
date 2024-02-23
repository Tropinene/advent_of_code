if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()

    dep_dict = {}
    for line in data:
        lst = line.strip().split()
        if dep_dict.get(lst[-3]) is None:
            dep_dict[lst[-3]] = []
        dep_dict[lst[-3]].append(lst[1])
        if dep_dict.get(lst[1]) is None:
            dep_dict[lst[1]] = []

    p1, waiting = [], []
    for k in dep_dict.keys():
        if not dep_dict[k]:
            waiting.append(k)

    while len(waiting) > 0:
        waiting.sort()
        p1.append(waiting[0])
        waiting = waiting[1:]

        for k in dep_dict.keys():
            if all(element in p1 for element in dep_dict[k]) and k not in p1 and k not in waiting:
                waiting.append(k)

    res = ''.join(p1)
    print(f"[Part1] : {res}")

