if __name__ == '__main__':
    entries = [int(x.strip()) for x in open('input.txt', 'r').readlines()]

    for i in entries:
        if (2020 - i) in entries:
            print(f"[Part1] : {i*(2020-i)}")
            break

    for i in range(len(entries)):
        for j in range(i, len(entries)):
            for k in range(j, len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    print(f"[Part2] : {entries[i]*entries[j]*entries[k]}")
                    quit()
