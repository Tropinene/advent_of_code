def main():
    numbers = [1, 20, 11, 6, 12, 0]
    spoken_indices = {num: idx for idx, num in enumerate(numbers[:-1])}
    print(spoken_indices)

    while len(numbers) < 2020:
        last_num = numbers[-1]
        if last_num not in spoken_indices:
            numbers.append(0)
        else:
            last_index = spoken_indices[last_num]
            numbers.append(len(numbers) - last_index - 1)
        spoken_indices[numbers[-2]] = len(numbers) - 2

    print(f"[Part1] : {numbers[-1]}")

    while len(numbers) < 30000000:
        last_num = numbers[-1]
        if last_num not in spoken_indices:
            numbers.append(0)
        else:
            last_index = spoken_indices[last_num]
            numbers.append(len(numbers) - last_index - 1)
        spoken_indices[numbers[-2]] = len(numbers) - 2

    print(f"[Part2] : {numbers[-1]}")


if __name__ == '__main__':
    main()