def gen_A(n):
    return n * 16807 % 2147483647


def gen_B(n):
    return n * 48271 % 2147483647


if __name__ == '__main__':
    a, b = 591, 393
    p1 = 0
    for idx in range(40000000):
        if idx % 10000000 == 0:
            print(f"Processing... Now round {idx}")
        a, b = gen_A(a), gen_B(b)
        binary_a, binary_b = format(a & 0xFFFF, '016b'), format(b & 0xFFFF, '016b')
        if binary_a == binary_b:
            p1 += 1
    print(f"[Part1] : {p1}")

    a, b = 591, 393
    p2 = 0
    for idx in range(5000000):
        if idx % 1000000 == 0:
            print(f"Processing... Now round {idx}")
        a, b = gen_A(a), gen_B(b)
        while a % 4:
            a = gen_A(a)
        while b % 8:
            b = gen_B(b)
        binary_a, binary_b = format(a & 0xFFFF, '016b'), format(b & 0xFFFF, '016b')
        if binary_a == binary_b:
            p2 += 1
    print(f"[Part2] : {p2}")
