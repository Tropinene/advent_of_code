from queue import Queue


def _knot_hash(s):
    length = [ord(x) for x in list(s)] + [17, 31, 73, 47, 23]
    circle = [x for x in range(256)]
    circle, last_skip, last_current = knot_hash(circle, length, 0, 0)
    for _ in range(63):
        circle, last_skip, last_current = knot_hash(circle, length, last_skip, last_current)

    dense_hash = ""
    for i in range(16):
        num = 0
        for j in range(16):
            num ^= circle[i * 16 + j]
        dense_hash += hex(num)[2:].zfill(2)
    return dense_hash


def knot_hash(circle, length, skip, current):
    for l in length:
        if current + l <= 256:
            slice = circle[current:current + l]
            slice = slice[::-1]
            circle = circle[:current] + slice + circle[current + l:]
        else:
            tmp1 = circle[current:]
            exceed = current + l - 256
            tmp2 = circle[:exceed]
            slice = tmp1 + tmp2
            slice = slice[::-1]
            circle = slice[-exceed:] + circle[exceed:current] + slice[:l - exceed]
        current = (current + skip + l) % 256
        skip += 1
    return circle, skip, current


def adjcant(location, r, c):
    dire = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    valid = []
    for d in dire:
        x, y = location[0] + d[0], location[1] + d[1]
        if 0 <= x < r and 0 <= y < c:
            valid.append((x, y))
    return valid


if __name__ == '__main__':
    hex_to_bin_mapping = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
    }

    p1 = 0
    inp = "uugsqrei"
    binarys = []
    for idx in range(128):
        hash = _knot_hash(inp + '-' + str(idx))
        binary_string = ''.join(hex_to_bin_mapping[c] for c in hash)
        binarys.append(binary_string)
        num_lst = [int(x) for x in list(binary_string)]
        p1 += sum(num_lst)
    print(f"[Part1] : {p1}")

    p2, visited = 0, []
    group = Queue()

    rows, cols = len(binarys), len(binarys[0])
    in_group = False
    for i in range(rows):
        for j in range(cols):
            if not in_group and (i, j) not in visited and binarys[i][j] == '1':
                group.put((i, j))
                in_group = True

            while not group.empty():
                cur = group.get()
                if cur in visited:
                    continue
                visited.append(cur)
                neighbors = adjcant(cur, rows, cols)
                for n in neighbors:
                    if binarys[n[0]][n[1]] == '1':
                        group.put(n)

            if in_group:
                p2 += 1
                in_group = False
    print(f"[Part2] : {p2}")
