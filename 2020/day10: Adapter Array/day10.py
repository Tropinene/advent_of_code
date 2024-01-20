def find_joltage_distribution(adapters: list[int]) -> int:
    adapters.sort()
    joltage_differences = {1: 0, 2: 0, 3: 1}

    current_joltage = 0
    for adapter in adapters:
        difference = adapter - current_joltage
        joltage_differences[difference] += 1
        current_joltage = adapter

    return joltage_differences[1] * joltage_differences[3]


def count_arrangements(adapters: list[int]) -> int:
    adapters.sort()
    adapters = [0] + adapters + [adapters[-1] + 3]
    arrangements_count = [0] * len(adapters)
    arrangements_count[0] = 1

    for i in range(1, len(adapters)):
        for j in range(i):
            if adapters[i] - adapters[j] <= 3:
                arrangements_count[i] += arrangements_count[j]

    return arrangements_count[-1]


def main():
    adapters = [int(line.strip()) for line in open('input.txt', 'r').readlines()]

    result = find_joltage_distribution(adapters)
    print(f"[Part1] : {result}")

    result = count_arrangements(adapters)
    print(f"[Part2] : {result}")


if __name__ == '__main__':
    main()
