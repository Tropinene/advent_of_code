def count_row(s: str) -> int:
    l, h = 0, 127
    for c in s:
        if c == 'F':
            h = (l + h) // 2
        else:
            l = (l + h) // 2 + 1
    return l


def count_col(s: str) -> int:
    l, h = 0, 7
    for c in s:
        if c == 'L':
            h = (l + h) // 2
        else:
            l = (l + h) // 2 + 1
    return l


def find_missing_seat(seat_ids: list) -> int:
    sorted_seat_ids = sorted(seat_ids)

    for i in range(len(sorted_seat_ids) - 1):
        if sorted_seat_ids[i + 1] - sorted_seat_ids[i] > 1:
            return sorted_seat_ids[i] + 1
    return -1


def main():
    seats = [x.strip() for x in open('input.txt', 'r').readlines()]

    seat_ids = []
    for seat in seats:
        row = count_row(seat[:7])
        col = count_col(seat[7:])
        seat_ids.append(row*8+col)
    print(f"[Part1] : {max(seat_ids)}")
    print(f"[Part2] : {find_missing_seat(seat_ids)}")


if __name__ == '__main__':
    main()
