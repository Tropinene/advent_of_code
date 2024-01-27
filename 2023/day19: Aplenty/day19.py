def process_rule_body(body_str: str) -> list:
    res = []
    body_lst = body_str.split(',')
    for item in body_lst:
        if ':' in item:
            condition, entry = item.split(':')
            if '<' in condition:
                name, num = condition.split('<')
                res.append((name, '<', int(num), entry))
            else:
                name, num = condition.split('>')
                res.append((name, '>', int(num), entry))
        else:
            res.append(item)
    return res


def process_workflow(workflow_str: str) -> dict:
    res = {}
    items = workflow_str.split(',')
    for item in items:
        name, value = item.split('=')
        res[name] = int(value)
    return res


def parse_file():
    lines = open('input.txt', 'r').read()
    part1, part2 = lines.split('\n\n')

    unprocessed_rules = part1.split('\n')
    rules = {}
    for line in unprocessed_rules:
        name, body = line.split('{')
        rule_body = process_rule_body(body[:-1])
        rules[name] = rule_body

    origin_workflow = [line[1:-1] for line in part2.split('\n')]
    workflows = []
    for workflow in origin_workflow:
        workflows.append(process_workflow(workflow))
    return rules, workflows


def check(rules: dict, workflow: dict) -> bool:
    def process_rule(rule):
        if type(rule) == str:
            return rule
        variable, comparator, value, next_rule = rule
        if (comparator == '<' and workflow[variable] < value) or (comparator == '>' and workflow[variable] > value):
            return next_rule
        return None

    cur_rule = rules['in']
    while True:
        for item in cur_rule:
            result = process_rule(item)
            if result is None:
                continue
            if result == 'A':
                return True
            elif result == 'R':
                return False
            else:
                cur_rule = rules[result]
                break


def main():
    rules, workflows = parse_file()

    p1 = 0
    for workflow in workflows:
        if check(rules, workflow):
            p1 += sum(item for item in workflow.values())
    print(f"[Part1] : {p1}")

    # todo Part2 使用广度优先算法应该可解


if __name__ == '__main__':
    main()

