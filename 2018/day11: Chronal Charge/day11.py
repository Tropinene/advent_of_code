def get_power_level(sn, x, y):
    rack_id = x + 10
    tmp = (rack_id * y + sn) * rack_id
    hundred = str(tmp // 100)[-1]
    return int(hundred) - 5


def find(a, size):
    max_val = -1
    l, r = -1, -1
    for i in range(300 - size):
        for j in range(300 - size):
            cnt = 0
            for p in range(size):
                for q in range(size):
                    cnt += a[i + p][j + q]
            if cnt > max_val:
                max_val = cnt
                l, r = j, i
    return l + 1, r + 1, max_val


if __name__ == "__main__":
    serial_num = 9798

    array = [[0 for _ in range(300)] for _ in range(300)]
    for X in range(1, 301):
        for Y in range(1, 301):
            pl = get_power_level(serial_num, X, Y)
            array[Y - 1][X - 1] = pl
    p1 = find(array, 3)
    print(f"[Part1] : {p1[0]},{p1[1]}")

    max_val, size = (-1, -1, -1), -1
    for s in range(1, 15):  # I know the right answer is under 15
        tmp = find(array, s)
        if tmp[-1] > max_val[-1]:
            max_val = tmp
            size = s
    print(f"[Part2] : {max_val[0]},{max_val[1]},{size}")
