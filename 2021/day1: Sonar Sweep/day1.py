def count_increase(depths: list[int]) -> int:
    cnt = 0
    for idx in range(1, len(depths)):
        if depths[idx] > depths[idx-1]:
            cnt += 1
    return cnt


def count_three_increase(depths: list[int]) -> int:
    cnt = 0
    for idx in range(2, len(depths)-1):
        if depths[idx-2]+depths[idx-1]+depths[idx] < depths[idx-1]+depths[idx]+depths[idx+1]:
            cnt += 1
    return cnt


def main():
    datas = [int(x.strip()) for x in open('input.txt', 'r').readlines()]

    print(f"[Part1] : {count_increase(datas)}")
    print(f"[Part2] : {count_three_increase(datas)}")


if __name__ == '__main__':
    main()
