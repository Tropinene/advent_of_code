import re


def cnt_length(s: str) -> int:
    cur_, res = 0, ""
    left = s.find('(', cur_)
    right = s.find(')', cur_)
    while left != -1:
        res += s[cur_:left]
        char_num, repeat_times = s[left+1:right].split('x')
        char_num, repeat_times = int(char_num), int(repeat_times)
        res += s[right+1:right+1+char_num] * repeat_times
        cur_ = right + char_num + 1
        left = s.find('(', cur_)
        right = s.find(')', cur_)

    if cur_ == 0:
        res = s
    else:
        res += s[cur_:]
    return len(res)


def cnt_length2(s: str) -> int:
    print(s)
    cur_ = 0
    left = s.find('(', cur_)
    if left == -1:
        return len(s)
    right = s.find(')', cur_)

    char_num, repeat_times = s[left + 1:right].split('x')
    char_num, repeat_times = int(char_num), int(repeat_times)
    # print(s[:left])
    # print(s[right+char_num+1:])
    return cnt_length2(s[:left]) + cnt_length2(s[right+1:right+char_num+1]) + cnt_length2(s[right+char_num+1:])


def main():
    # line = open('input.txt', 'r').readline().strip()
    line = "(6x1)(1x3)A"
    p1 = cnt_length(line)
    print(f"[Part1] : {p1}")

    p2 = cnt_length2(line)
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
