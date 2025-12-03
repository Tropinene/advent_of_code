def parse_input(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()

    blocks = content.split('\n\n')
    workflow_lines = blocks[0].split('\n')
    part_lines = blocks[1].split('\n')

    workflows = {}
    for line in workflow_lines:
        name, rest = line[:-1].split('{')
        rules_raw = rest.split(',')
        rules = []
        for rule_str in rules_raw:
            if ':' in rule_str:
                condition, target = rule_str.split(':')
                if '<' in condition:
                    cat, val = condition.split('<')
                    op = '<'
                else:
                    cat, val = condition.split('>')
                    op = '>'
                rules.append({'type': 'cmp', 'cat': cat, 'op': op, 'val': int(val), 'target': target})
            else:
                rules.append({'type': 'jump', 'target': rule_str})
        workflows[name] = rules

    parts = []
    for line in part_lines:
        segments = line[1:-1].split(',')
        part = {}
        for segment in segments:
            k, v = segment.split('=')
            part[k] = int(v)
        parts.append(part)

    return workflows, parts

def run_part1(workflows, parts):
    total = 0
    for part in parts:
        curr = 'in'
        while curr not in ('A', 'R'):
            rules = workflows[curr]
            matched = False
            for rule in rules:
                if rule['type'] == 'jump':
                    curr = rule['target']
                    matched = True
                    break
                else:
                    val = part[rule['cat']]
                    limit = rule['val']
                    if rule['op'] == '<':
                        if val < limit:
                            curr = rule['target']
                            matched = True
                            break
                    else:
                        if val > limit:
                            curr = rule['target']
                            matched = True
                            break
            if not matched:
                break
        
        if curr == 'A':
            total += sum(part.values())
    return total

def run_part2(workflows):
    def count(curr, ranges):
        if curr == 'R':
            return 0
        if curr == 'A':
            product = 1
            for lo, hi in ranges.values():
                product *= (hi - lo + 1)
            return product

        total = 0
        curr_ranges = ranges.copy()

        for rule in workflows[curr]:
            if rule['type'] == 'jump':
                total += count(rule['target'], curr_ranges)
                break
            
            cat = rule['cat']
            op = rule['op']
            val = rule['val']
            target = rule['target']
            lo, hi = curr_ranges[cat]
            
            true_range, false_range = None, None
            
            if op == '<':
                if lo < val:
                    true_range = (lo, min(hi, val - 1))
                if hi >= val:
                    false_range = (max(lo, val), hi)
            else:
                if hi > val:
                    true_range = (max(lo, val + 1), hi)
                if lo <= val:
                    false_range = (lo, min(hi, val))
            
            if true_range:
                next_ranges = curr_ranges.copy()
                next_ranges[cat] = true_range
                total += count(target, next_ranges)
            
            if false_range:
                curr_ranges[cat] = false_range
            else:
                break
        return total

    initial_ranges = {k: (1, 4000) for k in 'xmas'}
    return count('in', initial_ranges)

if __name__ == "__main__":
    workflows, parts = parse_input('input.txt')
    if workflows:
        print(f"[Part1]: {run_part1(workflows, parts)}")
        print(f"[Part2]: {run_part2(workflows)}")