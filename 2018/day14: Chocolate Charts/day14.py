if __name__ == '__main__':
    inp = 513401
    lst = [3, 7]
    a, b = 0, 1

    while len(lst) < inp + 10:
        n_receipt = lst[a] + lst[b]
        for i in str(n_receipt):
            lst.append(int(i))
        a, b = (a + lst[a] + 1) % len(lst), (b + lst[b] + 1) % len(lst)
    tmp = [str(x) for x in lst[-10:]]
    tmp = ''.join(tmp)
    print(f"[Part1] : {tmp}")

    lst = [3, 7]
    a, b = 0, 1
    while True:
        n_receipt = lst[a] + lst[b]
        for i in str(n_receipt):
            lst.append(int(i))
        a, b = (a + lst[a] + 1) % len(lst), (b + lst[b] + 1) % len(lst)

        tmp = [str(x) for x in lst[-10:]]
        tmp = ''.join(tmp)
        if len(lst) % 1000000 == 0:  # 20286858
            print(len(lst), tmp)
        if str(inp) in tmp:
            print(f"[Part2] : {len(lst) - len(str(inp)) - 1}")
            break
