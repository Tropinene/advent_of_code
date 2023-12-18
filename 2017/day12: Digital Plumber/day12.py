from queue import Queue


def get_group(name, dic):
    group = [name]
    check_lst = Queue()
    for item in dic[name]:
        check_lst.put(item)
    while not check_lst.empty():
        item = check_lst.get()
        if item not in group:
            group.append(item)
            for i in dic[item]:
                check_lst.put(i)
    return group


if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    dic = {}
    for line in data:
        start, connection = line.strip().split(' <-> ')
        connection = connection.split(', ')
        dic[start] = connection

    p1 = get_group('0', dic)
    print(f"[Part1] : {len(p1)}")

    checked = []
    checked.extend(p1)
    groups = [p1]
    for i in dic.keys():
        if i in checked:
            continue
        tmp = get_group(i, dic)
        checked.extend(tmp)
        groups.append(tmp)
    print(f"[Part2] : {len(groups)}")
