import copy


def arrangement(ori_lst: list) -> list:
    res = [None] * len(ori_lst)
    for val in ori_lst:
        next_lst = copy.deepcopy(ori_lst)

    return res


def main():
    origin_file = [int(x.strip()) for x in open('input.txt', 'r').readlines()]
    print(origin_file)
    print(arrangement(origin_file))
    # todo

if __name__ == '__main__':
    main()
