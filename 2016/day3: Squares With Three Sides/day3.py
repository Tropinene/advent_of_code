# part1: check whether the input 3 numbers can be a triangle
def is_triangle(sides: list) -> bool:
    sides = sorted(sides)
    return sides[0] + sides[1] > sides[2]


if __name__ == '__main__':
    file_path = './input.txt'
    data = open(file_path, 'r').readlines()
    lsts = []

    p1 = 0
    for line in data:
        lsts.append([int(x) for x in line.strip().split()])

    for lst in lsts:
        if is_triangle(lst):
            p1 += 1
    print(f'[Part1] : {p1}')

    p2 = 0
    t_ = [i[0] for i in lsts] + [i[1] for i in lsts] + [i[2] for i in lsts]
    for i in range(len(t_))[::3]:
        lst = [t_[i], t_[i + 1], t_[i + 2]]
        if is_triangle(lst):
            p2 += 1
    print(f'[Part2] : {p2}')
