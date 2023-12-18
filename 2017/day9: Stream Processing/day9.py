def count_bracket(line, is_part2):
    scale, stack = 0, []
    point = 0
    is_garbage, is_ignored = False, False
    for i in line:
        if is_ignored:
            is_ignored = False
            continue

        if i == '!':
            is_ignored = True

        if i == '<':
            if is_part2 and not is_garbage:
                point -= 1
            is_garbage = True
        elif i == '>':
            is_garbage = False
        if is_garbage and not is_ignored:
            if not is_part2:
                continue
            # when it starts to be garbage, point will +1, you should minus it before
            point += 1

        if not is_part2:
            if i == '{':
                stack.append(i)
                scale += 1
            elif i == '}':
                stack.pop()
                point += scale
                scale -= 1
    return point


if __name__ == '__main__':
    data = open('input.txt', 'r').readline()

    p1 = count_bracket(data.strip(), False)
    print(f"[Part1] : {p1}")

    p2 = count_bracket(data.strip(), True)
    print(f"[Part2] : {p2}")
