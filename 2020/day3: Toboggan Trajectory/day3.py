def count_trees(right, down):
    cnt = 0
    col, row = 0, 0
    while row < len(tree_map) - 1:
        col = (col + right) % len(tree_map[0])
        row += down
        if tree_map[row][col] == '#':
            cnt += 1
    return cnt


if __name__ == '__main__':
    tree_map = [x.strip() for x in open('input.txt', 'r').readlines()]

    p1 = count_trees(3, 1)
    print(f"[Part1] : {p1}")

    p2 = count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2)
    print(f"[Part2] : {p2}")
