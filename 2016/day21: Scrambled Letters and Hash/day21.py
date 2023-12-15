# part1: input string and do some operations
# part2: reverse

if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    input_str = list("abcdefgh")

    for line in data:
        lst = line.strip().split()
        if line.startswith("swap position"):
            x, y = int(lst[2]), int(lst[-1])
            input_str[x], input_str[y] = input_str[y], input_str[x]
        elif line.startswith("swap letter"):
            x, y = lst[2], lst[-1]
            for idx, i in enumerate(input_str):
                if i == x:
                    input_str[idx] = y
                elif i == y:
                    input_str[idx] = x
        elif line.startswith("move position"):
            x, y = int(lst[2]), int(lst[-1])
            tmp = input_str.pop(x)
            input_str.insert(y, tmp)
        elif line.startswith("rotate based"):
            idx = input_str.index(lst[-1])
            l = len(input_str)
            if idx >= 4:
                offset = -((idx + 2) % l)
            else:
                offset = -((idx + 1) % l)
            input_str = input_str[offset:] + input_str[:offset]
        elif line.startswith("rotate"):
            offset = int(lst[2])
            if lst[1] == 'right':
                offset = -offset
            input_str = input_str[offset:] + input_str[:offset]
        elif line.startswith("reverse"):
            x, y = int(lst[2]), int(lst[-1])
            tmp = input_str[x:y+1]
            tmp = tmp[::-1]
            input_str = input_str[:x] + tmp + input_str[y+1:]

    p1 = ''.join(input_str)
    print(f"[Part1] : {p1}")

    data = data[::-1]
    input_str = list("fbgdceah")
    for line in data:
        lst = line.strip().split()
        if line.startswith("swap position"):
            x, y = int(lst[2]), int(lst[-1])
            input_str[x], input_str[y] = input_str[y], input_str[x]
        elif line.startswith("swap letter"):
            x, y = lst[2], lst[-1]
            for idx, i in enumerate(input_str):
                if i == x:
                    input_str[idx] = y
                elif i == y:
                    input_str[idx] = x
        elif line.startswith("move position"):
            x, y = int(lst[-1]), int(lst[2])
            tmp = input_str.pop(x)
            input_str.insert(y, tmp)
        elif line.startswith("rotate based"):
            idx = input_str.index(lst[-1])
            l = len(input_str)
            if idx == 0: offset = 1
            if idx == 1: offset = 1
            if idx == 2: offset = 6
            if idx == 3: offset = 2
            if idx == 4: offset = 7
            if idx == 5: offset = 3
            if idx == 6: offset = 8
            if idx == 7: offset = 4
            input_str = input_str[offset:] + input_str[:offset]
        elif line.startswith("rotate"):
            offset = int(lst[2])
            if lst[1] == 'left':
                offset = -offset
            input_str = input_str[offset:] + input_str[:offset]
        elif line.startswith("reverse"):
            x, y = int(lst[2]), int(lst[-1])
            tmp = input_str[x:y+1]
            tmp = tmp[::-1]
            input_str = input_str[:x] + tmp + input_str[y+1:]

    p2 = ''.join(input_str)
    print(f"[Part2] : {p2}")
