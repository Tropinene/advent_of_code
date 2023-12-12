def has_symmetric_four_chars(input_string, n):
    length = len(input_string)
    flag, res = False, []
    for i in range(length - n + 1):
        substring = input_string[i:i + n]
        if substring == substring[::-1] and len(set(substring)) > 1:
            flag = True
            res.append(substring)
    return flag, res


def split_string_by_brackets(input_string):
    inside_brackets = []
    outside_brackets = []

    inside_flag = False
    current_part = ""

    for char in input_string:
        if char == '[':
            inside_flag = True
            if current_part:
                outside_brackets.append(current_part)
                current_part = ""
        elif char == ']':
            inside_flag = False
            if current_part:
                inside_brackets.append(current_part)
                current_part = ""
        else:
            current_part += char

    # 处理最后一个部分
    if current_part:
        if inside_flag:
            inside_brackets.append(current_part)
        else:
            outside_brackets.append(current_part)

    return inside_brackets, outside_brackets


def support_tls(line):
    ip, out = split_string_by_brackets(line)
    flag1, flag2 = True, False
    for i in ip:
        flag, _ = has_symmetric_four_chars(i, 4)
        if flag:
            flag1 = False
            break
    if flag1:
        for i in out:
            flag, _ = has_symmetric_four_chars(i, 4)
            if flag:
                flag2 = True
                break
    return flag1 and flag2


def support_ssl(line):
    ip, out = split_string_by_brackets(line)
    flag1, flag2 = False, False
    aba, bab = [], []
    for i in ip:
        flag, tmp = has_symmetric_four_chars(i, 3)
        if flag:
            flag1 = True
        aba.extend(tmp)
    if flag1:
        for i in out:
            flag, tmp = has_symmetric_four_chars(i, 3)
            if flag:
                flag2 = True
            bab.extend(tmp)

    if flag1 and flag2:
        for i in aba:
            for j in bab:
                if i[0] == j[1] and i[1] == j[0]:
                    return True
    return False


if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    p1, p2 = 0, 0

    for line in data:
        if support_tls(line.strip()):
            p1 += 1
        if support_ssl(line.strip()):
            p2 += 1

    print(f'[Part1] : {p1}')
    print(f'[Part2] : {p2}')
