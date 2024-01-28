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
    for i in range(1,len(cups)):
        cup = cups[(idx_1+i)%len(cups)]
        print(cup, end='')
    print()


if __name__ == "__main__":
    main()
