def rotate_string(input_str, num_shift):
    num_shift = num_shift % len(input_str)
    rotated_part = input_str[-num_shift:]
    remaining_part = input_str[:-num_shift]
    rotated_string = rotated_part + remaining_part

    return rotated_string


def swap_by_position(input_str, pos1, pos2):
    lst = list(input_str)
    tmp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = tmp

    return ''.join(lst)


def dance(s, mvs):
    for m in mvs:
        if m[0] == 's':
            offset = int(m[1:])
            s = rotate_string(s, offset)
        elif m[0] == 'x':
            a, b = m[1:].split('/')
            a, b = int(a), int(b)
            s = swap_by_position(s, a, b)
        elif m[0] == 'p':
            a, b = m[1:].split('/')
            idx_a, idx_b = s.index(a), s.index(b)
            s = swap_by_position(s, idx_a, idx_b)

    return s


if __name__ == '__main__':
    data = open('input.txt', 'r').readline()
    moves = data.strip().split(',')

    programs = 'abcdefghijklmnop'
    p1 = dance(programs, moves)
    print(f"[Part1] : {p1}")

    checklst = []
    for i in range(1000000000):
        checklst.append(programs)
        programs = dance(programs, moves)
        if programs == checklst[0] and i:
            programs = checklst[1000000000 % (i + 1)]
            break
    print(f"[Part2] : {programs}")
