def is_valid(base: list[int], num: int) -> bool:
    for i in range(25):
        for j in range(i, 25):
            if base[i] + base[j] == num:
                return True
    return False


def find_encryption_weakness(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        cnt = 0
        idx = i
        while cnt < target:
            cnt += nums[idx]
            if cnt == target:
                largest = max(nums[i:idx+1])
                smallest = min(nums[i:idx+1])
                return largest + smallest
            idx += 1


def main():
    datas = [int(x.strip()) for x in open("input.txt", "r").readlines()]

    invalid_num = -1
    for i in range(25, len(datas)):
        if not is_valid(datas[i-25:i], datas[i]):
            invalid_num = datas[i]
            break
    print(f"[Part1] : {invalid_num}")

    p2 = find_encryption_weakness(datas, invalid_num)
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
