def parse_file() -> (list, list):
    data = open('input.txt', 'r').read()
    player1, player2 = data.split('\n\n')

    player1 = [int(x) for x in player1.split('\n')[1:]]
    player2 = [int(x) for x in player2.split('\n')[1:]]
    return player1, player2


def count_score(lst: list) -> int:
    l, res = len(lst), 0
    for idx, num in enumerate(lst):
        res += (l - idx) * num
    return res


def solve1(lst1: list, lst2: list) -> list:
    player1, player2 = lst1.copy(), lst2.copy()
    while len(player1) != 0 and len(player2) != 0:
        card1, card2 = player1.pop(0), player2.pop(0)
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    return player1+player2


def sub_game(lst1, lst2) -> bool:
    player1, player2 = lst1.copy(), lst2.copy()
    while len(player1) != 0 and len(player2) != 0:
        card1, card2 = player1.pop(0), player2.pop(0)
        if len(player1) == card1 or len(player2) == card2:
            if sub_game(player1, player2):
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
            continue
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    return len(player1) > len(player2)


def solve2(lst1: list, lst2: list) -> list:
    player1, player2 = lst1.copy(), lst2.copy()
    while len(player1) != 0 and len(player2) != 0:
        card1, card2 = player1.pop(0), player2.pop(0)
        if len(player1) == card1 or len(player2) == card2:
            if sub_game(player1, player2):
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
            continue
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    return player1+player2


def main():
    player1, player2 = parse_file()

    p1 = count_score(solve1(player1, player2))
    print(f"[Part1] : {p1}")

    p2 = count_score(solve2(player1, player2))
    print(f"[Part2] : {p2}")


if __name__ == '__main__':
    main()