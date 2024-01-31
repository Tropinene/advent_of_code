def parse_file() -> dict:
    lines = [line.strip() for line in open('input.txt', 'r').readlines()]

    cards = {}
    for line in lines:
        card, bid_str = line.split()
        cards[card] = int(bid_str)
    return cards


def char_count(s: str) -> dict:
    res = {}
    for c in s:
        res[c] = res.get(c, 0) + 1
    return res


def sort_cards(cards: list, is_part2: bool) -> list:
    five_a_kind, four_a_kind, full_house = [], [], []
    three_a_kind, two_pair, one_pair, high_card = [], [], [], []

    for card in cards:
        char_cnt = char_count(card)
        if is_part2 and char_cnt.get('J'):
            tmp = [char_cnt[x] for x in char_cnt.keys() if x != 'J']
            if len(tmp) > 0:
                num_char = len(char_cnt) - 1
                max_num = max(tmp) + char_cnt.get('J')
            else:
                num_char = len(char_cnt)
                max_num = char_cnt.get('J')
        else:
            num_char = len(char_cnt)
            max_num = max(char_cnt.values())

        if num_char == 1:
            five_a_kind.append(card)
        elif num_char == 2:
            if max_num == 4:
                four_a_kind.append(card)
            else:
                full_house.append(card)
        elif num_char == 3:
            if max_num == 3:
                three_a_kind.append(card)
            else:
                two_pair.append(card)
        elif num_char == 4:
            one_pair.append(card)
        else:
            high_card.append(card)

    return _sort(five_a_kind, is_part2) + _sort(four_a_kind, is_part2) \
        + _sort(full_house, is_part2) + _sort(three_a_kind, is_part2) \
        + _sort(two_pair, is_part2) + _sort(one_pair, is_part2) + _sort(high_card, is_part2)


def _sort(lst: list, is_part2: bool) -> list:
    if is_part2:
        sorting_order = "AKQT98765432J"
    else:
        sorting_order = "AKQJT98765432"
    sorted_list = sorted(lst, key=lambda x: [sorting_order.index(c) for c in x])
    return sorted_list


def main():
    cards = parse_file()
    sorted_cards = sort_cards(list(cards.keys()), False)
    p1 = 0
    for idx, card in enumerate(sorted_cards):
        p1 += (len(sorted_cards) - idx) * cards.get(card)
    print(f"[Part1] : {p1}")

    sorted_cards = sort_cards(list(cards.keys()), True)
    p2 = 0
    for idx, card in enumerate(sorted_cards):
        p2 += (len(sorted_cards) - idx) * cards.get(card)
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()
