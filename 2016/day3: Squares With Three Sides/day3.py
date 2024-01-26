# part1: check whether the input 3 numbers can be a triangle
def is_triangle(sides: list) -> bool:
    # if lst[0] + lst[1] > lst[2] and lst[1] + lst[2] > lst[0] and lst[0] + lst[2] > lst[1]:
    if abs(lst[0] - lst[1]) < lst[2] < lst[0] + lst[1]:
        return True


if __name__ == '__main__':
    file_path = './input.txt'
    data = open(file_path, 'r').readlines()

    p1 = 0
    for line in data:
        lst = [int(x) for x in line.strip().split()]
        if is_triangle(lst):
            p1 += 1
    print(f'[Part1] : {p1}')

    # vertical = [[], [], []]
    # p2 = 0
    # for line in data:
    #     lst = [int(x) for x in line.strip().split()]
    #     for i in range(3):
    #         vertical[i].append(lst[i])
    # for i in range(3):
    #     cur = vertical[i]
    #     for i in range(len(cur)):
    #         for j in range(i, len(cur)):
    #             in_range = sum(1 for num in cur[j+1:] if abs(cur[i]-cur[j]) < num < cur[i]+cur[j])
    #             p2 += in_range
    # print(f'[Part2] : {p2}')