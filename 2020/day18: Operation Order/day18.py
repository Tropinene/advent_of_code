def special_cal(inp_str: str) -> int:
    res = 0
    num_stack, op_stack = [], []
    inp_str = inp_str.replace(' ', '')

    for i in inp_str[::-1]:
        if i.isdigit():
            num_stack.append(int(i))
        else:
            op_stack.append(i)

    while len(op_stack):
        num1, num2 = num_stack.pop(), num_stack.pop()
        op = op_stack.pop()
        if op == '+':
            num1 += num2
        elif op == '*':
            num1 *= num2
        num_stack.append(num1)
    print(num_stack.pop())

    return res


def main():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]

    p1 = 0
    for line in lines:
        p1 += special_cal(line)
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()
