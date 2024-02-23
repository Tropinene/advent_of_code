from collections import Counter


if __name__ == '__main__':
    ids = open('input.txt', 'r').readlines()

    two_l, three_l = 0, 0
    for id in ids:
        word = Counter(id.strip())
        if any(cnt == 2 for cnt in word.values()):
            two_l += 1
        if any(cnt == 3 for cnt in word.values()):
            three_l += 1

    print(f"[Part1] : {two_l * three_l}")

    for i in range(len(ids[0])):
        box = []
        for id in ids:
            slice = id.strip()[:i] + id.strip()[i+1:]
            if slice in box:
                print(f"[Part2] : {slice}")
                quit()
            box.append(slice)

