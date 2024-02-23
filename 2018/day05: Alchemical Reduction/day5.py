def remove_polymer(s):
    while True:
        new_str = s
        for idx in range(1, len(s)):
            if abs(ord(s[idx]) - ord(s[idx-1])) == abs(ord('a') - ord('A')):
                new_str = new_str.replace(s[idx-1:idx+1], '')
        if new_str == s:
            return len(new_str)
        s = new_str


if __name__ == '__main__':
    input_str = open('input.txt', 'r').readline().strip()

    print(f"[Part1] : {remove_polymer(input_str)}")

    min_len = -1
    for offset in range(26):
        tmp = input_str
        tmp = tmp.replace(chr(ord('a') + offset), '')
        tmp = tmp.replace(chr(ord('A') + offset), '')
        length = remove_polymer(tmp)

        if min_len == -1 or min_len > length:
            min_len = length
    print(f"[Part2] : {min_len}")
