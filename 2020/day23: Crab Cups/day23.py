def crab_cups(cups, moves):
    max_cup = max(cups)
    cups_dict = {cup: cups[(i + 1) % len(cups)] for i, cup in enumerate(cups)}

    current_cup = cups[0]
    for _ in range(moves):
        pick_up = [cups_dict[current_cup]]
        pick_up.append(cups_dict[pick_up[-1]])
        pick_up.append(cups_dict[pick_up[-1]])

        destination_cup = current_cup - 1
        while destination_cup in pick_up or destination_cup < 1:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = max_cup

        cups_dict[current_cup] = cups_dict[pick_up[-1]]
        cups_dict[pick_up[-1]] = cups_dict[destination_cup]
        cups_dict[destination_cup] = pick_up[0]

        current_cup = cups_dict[current_cup]

    return cups_dict


def find_next_labels(cups_dict):
    next_cup_1 = cups_dict[1]
    next_cup_2 = cups_dict[next_cup_1]

    return next_cup_1, next_cup_2



def move(cups: list, cur_cup: int) -> (int, list):
    cur_idx = cups.index(cur_cup)
    num_cups = len(cups)
    pick_cups = [cups[(cur_idx + i) % num_cups] for i in range(1, 4)]

    des_cup = cur_cup - 1
    if des_cup < min(cups):
        des_cup = max(cups)
    while des_cup in pick_cups:
        des_cup -= 1
        if des_cup < min(cups):
            des_cup = max(cups)
    next_cup_idx = cups.index(des_cup)
    # print(f"[+] picked cups: {pick_cups}")
    # print(f"[+] destination cups: {des_cup}")
    new_cups = [des_cup] + pick_cups
    for i in range(0, num_cups):
        idx = (next_cup_idx + i) % num_cups
        if cups[idx] not in new_cups:
            new_cups.append(cups[idx])

    next_idx = (new_cups.index(cur_cup) + 1) % num_cups
    return new_cups[next_idx], new_cups


def main():
    cups = [int(x) for x in list("137826495")]
    cur = cups[0]
    for rnd in range(100):
        # print(f"[+] Round_{rnd}")
        cur, cups = move(cups, cur)
        # print(f"[+] Next cup is {cur}, cups now: {cups}")
        # print()
    idx_1 = cups.index(1)
    print("[Part1] : ", end='')
    for i in range(1, len(cups)):
        cup = cups[(idx_1 + i) % len(cups)]
        print(cup, end='')
    print()

    cups = [int(x) for x in list("137826495")]
    cups += list(range(10, 1000001))

    final_cups_dict = crab_cups(cups, 10000000)
    next_label_1, next_label_2 = find_next_labels(final_cups_dict)

    print(f"[Part2] : {next_label_1 * next_label_2}")

if __name__ == "__main__":
    main()
