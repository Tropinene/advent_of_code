# part1: check whether the input 3 numbers can be a triangle

if __name__ == '__main__':
    file_path = './input.txt'
    data = open(file_path, 'r').readlines()

    cnt = 0
    for line in data:
        lst = line.strip().split()
        lst = [int(x) for x in lst]

        if lst[0] + lst[1] > lst[2] and lst[1] + lst[2] > lst[0] and lst[0] + lst[2] > lst[1]:
            cnt += 1
    print(f'[Part1] : {cnt}')
