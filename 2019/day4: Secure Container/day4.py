def has_consecutive_duplicates(num):
    num_str = str(num)
    for idx, c in enumerate(num_str[:-1]):
        if c == num_str[idx+1]:
            return True
    return False

def has_no_decrease(num):
    num_str = str(num)
    return all(int(num_str[i]) <= int(num_str[i+1]) for i in range(len(num_str)-1))

def has_adjacent_pairs(num):
    num_str = str(num)
    count = 1
    has_valid_pair = False

    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            count += 1
        else:
            if count == 2:
                has_valid_pair = True
            count = 1
    # Check the last pair
    if count == 2:
        has_valid_pair = True

    return has_valid_pair

if __name__ == "__main__":
    p1, p2 = 0, 0
    for i in range(137683, 596253+1):
        if has_no_decrease(i):
            if has_consecutive_duplicates(i):
                p1 += 1
            if has_adjacent_pairs(i):
                p2 += 1
    print(f"[Part1] {p1}")
    print(f"[Part2] {p2}")
