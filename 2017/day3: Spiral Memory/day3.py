def ret_next_val(target):
    dic = {(0, 0): 1}
    current = (0, 0)
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    val = 1
    while val <= target:
        tmp = 0
        for d in direction:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if dic.get(neighbor):
                tmp += dic.get(neighbor)
        # todo 更新current的坐标，写一个函数得到，然后加到dic里去


if __name__ == '__main__':
    inp = 361527
    scale = 1
    while True:
        if scale ** 2 >= inp:
            break
        scale += 2

    gap = scale ** 2 - inp
    line = gap // (scale - 1)
    if line == 0:
        location = (scale // 2 - gap, -(scale // 2))
    elif line == 1:
        location = (-(scale // 2), -(scale // 2) + gap - scale + 1)
    elif line == 2:
        location = (-(scale // 2) + gap - scale * 2 + 2, scale // 2)
    elif line == 3:
        location = (scale // 2, scale // 2 - (gap - scale * 3 + 3))
    print(f"[Part1] : {abs(location[0]) + abs(location[1])}")

