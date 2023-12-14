# actually I am really confused with the title.

if __name__ == '__main__':
    elves = []
    for i in range(3005290):
        elves.append(i+1)

    cnt = 0
    while len(elves) > 1:
        if cnt == len(elves)-1:
            elves.pop(0)
        else:
            elves.pop(cnt+1)

        # Move to the next elf
        cnt += 1
        if cnt >= len(elves):
            cnt = 0

    print(f"[Part1] : {elves[0]}")