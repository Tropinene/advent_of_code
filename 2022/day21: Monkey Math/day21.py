def get_value(monkey: dict, name: str) -> int:
    val = monkey.get(name)
    if type(val) == int:
        return monkey.get(name)

    name1, op, name2 = val.split()
    if op == '+':
        return get_value(monkey, name1) + get_value(monkey, name2)
    elif op == '-':
        return get_value(monkey, name1) - get_value(monkey, name2)
    elif op == '*':
        return get_value(monkey, name1) * get_value(monkey, name2)
    else:
        return get_value(monkey, name1) // get_value(monkey, name2)


def solve_1(monkey: dict) -> int:
    name = 'root'
    return get_value(monkey, name)


def main():
    data = [x.strip().split(': ') for x in open('input.txt', 'r').readlines()]

    data_dict = {}
    while data:
        name, value = data.pop()
        if value.isdigit():
            value = int(value)
        data_dict[name] = value
    print(f"[Part1] : {solve_1(data_dict)}")
    # todo part2


if __name__ == '__main__':
    main()
