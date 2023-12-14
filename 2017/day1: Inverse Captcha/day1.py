# part1: count the consecutive number
# part2: count the number  s[i] = s[i+len/2]

if __name__ == '__main__':
    line = open("input.txt", 'r').readline().strip()

    p1, p2 = 0, 0
    length = len(line)
    offset = int(length / 2)
    for i in range(length):
        if line[i] == line[(i + 1) % length]:
            p1 += int(line[i])
        if line[i] == line[(i + offset) % length]:
            p2 += int(line[i])

    print(f"[Part1] : {p1}")
    print(f"[Part2] : {p2}")
