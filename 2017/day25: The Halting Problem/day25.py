import re


def parse_file() -> (int, dict):
    with open('input.txt', 'r') as file:
        content = file.read().split('\n\n')

    steps = int(re.findall(r'\d+', content[0])[0])

    rules = {}
    for state in content[1:]:
        options = []
        options_raw = state.split('If')
        name, options_raw = options_raw[0], options_raw[1:]

        name = name[name.index(':') - 1]

        for option_raw in options_raw:
            option_raw = option_raw.split('-')[1:]
            val = int(option_raw[0][option_raw[0].index('.') - 1])
            next_state = option_raw[2][option_raw[2].index('.') - 1]
            direction = 'right' if 'right' in option_raw[1] else 'left'
            options.append([val, direction, next_state])
        rules[name] = options

    return steps, rules


def go_write(rule: list, s_lst: list, idx: int) -> (list, int, str):
    cur_state = s_lst[idx]
    val, direction, next_state_name = rule[cur_state]

    s_lst[idx] = val
    if direction == 'right':
        idx += 1
    else:
        idx -= 1

    if idx >= len(s_lst):
        s_lst.append(0)
    elif idx < 0:
        s_lst = [0] + s_lst
        idx = 0

    return s_lst, idx, next_state_name


def machine(rules: dict, state_name: str, steps: int) -> int:
    s_lst, idx = [0], 0
    for _ in range(steps):
        rule = rules.get(state_name)
        s_lst, idx, state_name = go_write(rule, s_lst, idx)
    return sum(s_lst)


def main():
    steps, rules = parse_file()
    p1 = machine(rules, 'A', steps)
    print(f"[Part1] : {p1}")


if __name__ == '__main__':
    main()
