def find_loop_size(public_key: int, subject_number: int) -> int:
    value = 1
    loop_size = 0

    while value != public_key:
        value = (value * subject_number) % 20201227
        loop_size += 1

    return loop_size


def encrypt(loop_size: int, subject_number: int) -> int:
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value


def main():
    num1, num2 = 6930903, 19716708
    loop_size1 = find_loop_size(num1, 7)
    print(f"[Part1] : {encrypt(loop_size1, num2)}")


if __name__ == '__main__':
    main()
