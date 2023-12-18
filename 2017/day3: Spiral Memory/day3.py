def ret_next_val(target):
    dic = {(0, 0): 1}
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    idx, val = 1, 1
    while val <= target:
        tmp = 0
        current = trans2position(idx+1)
        for d in direction:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if dic.get(neighbor):
                tmp += dic.get(neighbor)
        dic[current] = tmp
        val = tmp
        idx += 1
    return val


def trans2position(val):
    scale = 1
    while True:
        if scale ** 2 >= val:
            break
        scale += 2

    gap = scale ** 2 - val
    line = gap // (scale - 1)
    if line == 0:
        location = (scale // 2 - gap, -(scale // 2))
    elif line == 1:
        location = (-(scale // 2), -(scale // 2) + gap - scale + 1)
    elif line == 2:
        location = (-(scale // 2) + gap - scale * 2 + 2, scale // 2)
    elif line == 3:
        location = (scale // 2, scale // 2 - (gap - scale * 3 + 3))

    return location


if __name__ == '__main__':
    inp = 361527
    loc = trans2position(inp)
    print(f"[Part1] : {abs(loc[0]) + abs(loc[1])}")

    print(f"[Part2] : {ret_next_val(inp)}")
