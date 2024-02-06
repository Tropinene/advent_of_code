import re


def parse_file() -> (dict, dict):
    lines = open('input.txt', 'r').readlines()

    bots, instruction = {}, {}
    for line in lines:
        if line.startswith('value'):
            matches = re.findall(r'\d+', line)
            matches = [int(item) for item in matches]
            if bots.get(matches[1]):
                bots[matches[1]].append(matches[0])
            else:
                bots[matches[1]] = [matches[0]]
        else:
            lst = line.strip().split()
            instruction[int(lst[1])] = (lst[5]+lst[6], lst[10]+lst[11])
    return bots, instruction


def solve(bots: dict, ins: tuple, bot_id: int, is_part2: bool) -> bool:
    low_next, high_next = ins
    if not is_part2:
        if 61 in bots[bot_id] and 17 in bots[bot_id]:
            print(f"[Part1] : {bot_id}")
            return True

    low, high = min(bots[bot_id]), max(bots[bot_id])
    bots[bot_id].remove(low)
    bots[bot_id].remove(high)

    match = re.findall(r'\d+', low_next)
    next_bot_id = int(match[0])
    if low_next.startswith('bot'):
        if bots.get(next_bot_id):
            bots[next_bot_id].append(low)
        else:
            bots[next_bot_id] = [low]
    else:
        if next_bot_id <= 2:
            output[next_bot_id].append(low)

    match = re.findall(r'\d+', high_next)
    next_bot_id = int(match[0])
    if high_next.startswith('bot'):
        if bots.get(next_bot_id):
            bots[next_bot_id].append(high)
        else:
            bots[next_bot_id] = [high]
    else:
        if next_bot_id <= 2:
            output[next_bot_id].append(low)

    return False


def main():
    bots, instructions = parse_file()
    while True:
        ins, bot_id = None, 0
        for key, val in bots.items():
            if len(val) == 2:
                ins, bot_id = instructions.get(key), key
                break
        if solve(bots, ins, bot_id, False):
            break

    while True:
        ins, bot_id = None, 0
        stop_flag = True
        for key, val in bots.items():
            if len(val) == 2:
                stop_flag = False
                ins, bot_id = instructions.get(key), key
                break
        if stop_flag:
            break
        solve(bots, ins, bot_id, True)
    p2 = output[0][0] * output[1][0] * output[2][0]
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    output = [[], [], []]
    main()
