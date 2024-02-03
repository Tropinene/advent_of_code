from collections import deque


def mix(lst, rounds) -> int:
    length = len(lst)
    zero = (0, lst.index(0))
    data = deque(
        [(number, index) for index, number in enumerate(lst)]
    )
    order = [n for n in lst]
    for _ in range(rounds):
        for i, number in enumerate(order):
            index = data.index((number, i))
            data.rotate(-index)
            value: tuple[int, int] = data.popleft()
            data.rotate(-value[0])
            data.appendleft(value)

    zero_index = data.index(zero)
    return sum(data[(zero_index + i) % length][0] for i in (1000, 2000, 3000))


def main():
    numbers = [int(x) for x in open('input.txt', 'r').readlines()]
    print(f"[Part1] : {mix(numbers, 1)}")

    numbers = [n*811589153 for n in numbers]
    print(f"[Part1] : {mix(numbers, 10)}")


if __name__ == '__main__':
    main()
