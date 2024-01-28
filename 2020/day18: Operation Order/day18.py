def calculate(expression: str, is_part2: bool) -> int:
    expression = expression.replace(" ", "")
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            tokens.append(expression[i:j])
            i = j
        else:
            tokens.append(expression[i])
            i += 1

    result, _ = evaluate_expression(tokens, is_part2)
    return result


def evaluate(op: str, a: int, b: int) -> int:
    if op == "+":
        return a + b
    elif op == "*":
        return a * b


def evaluate_expression(tokens: list, is_part2: bool) -> (int, int):
    stack = []
    i = 0

    while i < len(tokens):
        if tokens[i] == "(":
            if is_part2:
                sub_expression, tmp = evaluate_expression(tokens[i + 1:], True)
            else:
                sub_expression, tmp = evaluate_expression(tokens[i + 1:], False)
            i += tmp
            stack.append(sub_expression)
        elif tokens[i] == ")":
            if is_part2:
                return evaluate_stack_precedence(stack), i + 1
            return evaluate_stack(stack), i + 1
        else:
            if tokens[i].isdigit():
                stack.append(int(tokens[i]))
            else:
                stack.append(tokens[i])
        i += 1
    if is_part2:
        return evaluate_stack_precedence(stack), i
    return evaluate_stack(stack), i


def evaluate_stack(stack: list) -> int:
    if not stack:
        return 0

    res = stack.pop(0)
    while stack:
        op = stack.pop(0)
        if not stack:
            return res
        num = stack.pop(0)
        res = evaluate(op, res, num)

    return res


def evaluate_stack_precedence(stack: list) -> int:
    if not stack:
        return 0

    num_stack, op_stack = [], []
    i = 0
    while i < len(stack):
        if isinstance(stack[i], int):
            num_stack.append(stack[i])
        else:
            while op_stack and op_stack[-1] == "+":
                op = op_stack.pop()
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(evaluate(op, num1, num2))
            op_stack.append(stack[i])
        i += 1

    while op_stack and op_stack[-1] == "+":
        op = op_stack.pop()
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        num_stack.append(evaluate(op, num1, num2))
    while op_stack:
        op = op_stack.pop(0)
        num2 = num_stack.pop(0)
        num1 = num_stack.pop(0)
        num_stack.append(evaluate(op, num1, num2))

    return num_stack[0]


def main():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    p1, p2 = 0, 0
    for line in lines:
        p1 += calculate(line, False)
        p2 += calculate(line, True)
    print(f"[Part1] : {p1}")
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
