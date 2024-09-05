def solve() -> int:
    res = 1
    tiles_sides, tiles_names = [], []
    tiles = open('input.txt', 'r').read().split('\n\n')

    for tile in tiles:
        tile = tile.split('\n')
        name, tile = tile[0][5:9], tile[1:-1]

        f_col, l_col = '', ''
        for line in tile:
            f_col += line[0]
            l_col += line[-1]
        sides = [tile[0], tile[-1], f_col, l_col]
        tiles_names.append(name)
        tiles_sides.extend(sides)
    # 如何判断未完成
    # for i in range(0, len(tiles_sides), 4):
    #     cnt = 0
    #     for j in range(4):
    #         if tiles_sides[i+j] == tiles_sides[i+j][::-1]:
    #             break
    #         if tiles_sides.count(tiles_sides[i+j]) + tiles_sides.count(tiles_sides[i+j][::-1]) > 1:
    #             cnt += 1
    #     if cnt == 2:
    #         res *= int(tiles_names[i//4])
    return res


def main():
    p1 = solve()
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()
