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


if __name__ == '__main__':
    circle = [x for x in range(256)]
    length = open('input.txt', 'r').readline().strip().split(',')
    length = [int(x) for x in length]

    circle, _, _ = knot_hash(circle, length, 0, 0)
    print(f"[Part1] : {circle[0]*circle[1]}")

    data = open('input.txt', 'r').readline().strip()
    length = [ord(x) for x in data] + [17, 31, 73, 47, 23]
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
    print(f'[Part2] : {dense_hash}')
