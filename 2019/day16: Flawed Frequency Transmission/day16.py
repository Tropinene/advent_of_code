def fft_phase(signal):
    base_pattern = [0, 1, 0, -1]
    output_signal = []

    for i in range(len(signal)):
        pattern = [p for p in base_pattern for _ in range(i + 1)]
        pattern *= ((len(signal) // len(pattern)) + 1)
        pattern = pattern[1:len(signal) + 1]

        result = abs(sum(s * p for s, p in zip(signal, pattern))) % 10
        output_signal.append(result)

    return output_signal


def part1(input_signal, phases):
    signal = [int(digit) for digit in input_signal]

    for _ in range(phases):
        signal = fft_phase(signal)

    result = ''.join(map(str, signal[:8]))
    return result


def part2(input_signal, phases, repeat):
    signal = [int(digit) for digit in input_signal] * repeat
    offset = int(input_signal[:7])

    for _ in range(phases):
        for i in range(len(signal) - 2, offset - 1, -1):
            signal[i] = (signal[i] + signal[i + 1]) % 10

    result = ''.join(map(str, signal[offset:offset + 8]))
    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_data = file.read().strip()

    print(f"[Part 1] {part1(input_data, 100)}")
    print(f"[Part 2] {part2(input_data, 100, 10000)}")