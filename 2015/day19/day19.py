def findall(text, sub):
    position = []
    idx = text.find(sub)
    while idx != -1:
        position.append(idx)
        idx = text.find(sub, idx+1)
    return position


if __name__ == '__main__':
    lines = open('./eg.txt', 'r').readlines()
    s = lines[-1].strip()
    dic = {}
    for line in lines[:-2]:
        old, replace = line.strip().split(' => ')
        if dic.get(old) is None:
            dic[old] = []
        dic[old].append(replace)

    res = []
    for item in dic.keys():
        pos = findall(s, item)
        for p in pos:
            for replace in dic.get(item):
                new_s = s[:p] + replace + s[p+len(item):]
                if new_s not in res:
                    res.append(new_s)

    print(f"[Part1] : {len(res)}")


