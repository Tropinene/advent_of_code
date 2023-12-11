
def gen(num):
    return num * 252533 % 33554393


if __name__ == '__main__':
    cur = 20151125
    loc = (2981, 3075)
    times = (loc[0] + loc[1] - 2) * (loc[0] + loc[1] - 1) // 2 + loc[1] - 1
    for i in range(times):
        cur = gen(cur)
    print(f'[Part1] : {cur}')
