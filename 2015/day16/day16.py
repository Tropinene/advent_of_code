def getData(path):
    with open(path, 'r') as f:
        data = f.readlines()
        f.close()
    return data


if __name__ == '__main__':
    file_path = './input.txt'
    data = getData(file_path)

    gift = {}
    for line in data:
        aunt, gifts = line.strip().split(':', 1)
        tmp = {}
        items = gifts.strip().split(',')
        for item in items:
            name, num = item.strip().split(':')
            tmp[name] = int(num.strip())
        gift[aunt] = tmp

    target = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    for aunt, items in gift.items():
        flag = True
        for i in items.keys():
            if target.get(i) is None or items.get(i) != target.get(i):
                flag = False
                break
        if flag:
            print(f'[Part1] : {aunt}')
            break

    greater = ['cats', 'trees']
    fewer = ['pomeranians', 'goldfish']
    for aunt, items in gift.items():
        flag = True
        for i in items.keys():
            if target.get(i) is None:
                flag = False
                break
            if i in greater:
                if items.get(i) <= target.get(i):
                    flag = False
                    break
            elif i in fewer:
                if items.get(i) >= target.get(i):
                    flag = False
                    break
            else:
                if items.get(i) != target.get(i):
                    flag = False
                    break

        if flag:
            print(f'[Part2] : {aunt}')
            break

