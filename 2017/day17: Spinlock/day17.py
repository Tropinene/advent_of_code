if __name__ == '__main__':
    buffer = [0]

    cur = 0
    for i in range(1, 2018):
        cur = (cur + 354) % len(buffer) + 1
        buffer.insert(cur, i)
    print(f"[Part1] : {buffer[cur+1]}")

    zero_idx = 0
    after_zero = None
    buf_len, cur = 1, 0
    for j in range(1, 50000000 + 1):
        cur = (cur + 354) % buf_len + 1
        if cur <= zero_idx:
            zero_idx += 1
        if cur == zero_idx + 1:
            after_zero = j
        buf_len += 1
    print(f"[Part2] : {after_zero}")
