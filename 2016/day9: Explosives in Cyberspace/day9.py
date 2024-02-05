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


def main():
    line = open('input.txt', 'r').readline().strip()
    p1 = cnt_length(line)
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()
