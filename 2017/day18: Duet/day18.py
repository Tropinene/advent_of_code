if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()

    reg = {}
    idx, snd = 0, 0
    while idx < len(data):
        lst = data[idx].strip().split()
        if not reg.get(lst[1]):
            reg[lst[1]] = 0

        if lst[0] == 'set':
            if lst[2].isdigit() or lst[2][0] == '-':
                reg[lst[1]] = int(lst[2])
            else:
                reg[lst[1]] = reg[lst[2]]
        elif lst[0] == 'add':
            if lst[2].isdigit() or lst[2][0] == '-':
                reg[lst[1]] += int(lst[2])
            else:
                reg[lst[1]] += reg[lst[2]]
        elif lst[0] == 'mul':
            if lst[2].isdigit() or lst[2][0] == '-':
                reg[lst[1]] *= int(lst[2])
            else:
                reg[lst[1]] *= reg[lst[2]]
        elif lst[0] == 'mod':
            if lst[2].isdigit() or lst[2][0] == '-':
                reg[lst[1]] %= int(lst[2])
            else:
                reg[lst[1]] %= reg[lst[2]]
        elif lst[0] == 'jgz':
            if reg[lst[1]] > 0:
                idx += int(lst[2])
                continue
        elif lst[0] == 'snd':
            snd = reg[lst[1]]
        elif lst[0] == 'rcv':
            if reg[lst[1]]:
                print(f"[Part1] : {snd}")
                break
        else:
            pass

        idx += 1
