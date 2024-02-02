def parse_file() -> list:
    data = list(map(int, open('input.txt', 'r').readlines()))
    res = []
    for idx, val in enumerate(data):
        res.append((idx, val))
    return res


def mix(nums: list) -> list:
    l = len(nums)
    for idx, val in nums:
        new_idx = (idx + val + l) % l
        print(nums)
        quit()


def main():
    numbers = parse_file()
    mix(numbers)


if __name__ == '__main__':
    main()
