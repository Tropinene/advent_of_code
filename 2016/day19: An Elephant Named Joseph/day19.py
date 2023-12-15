# actually I am really confused with the title.

if __name__ == '__main__':
    elves = []
    for i in range(3001330):
        elves.append(i+1)

    cnt = 0
    while len(elves) > 1:
        if len(elves) % 10000 == 0:
            print(len(elves))
        if cnt == len(elves)-1:
            elves.pop(0)
        else:
            elves.pop(cnt+1)

        # Move to the next elf
        cnt += 1
        if cnt >= len(elves):
            cnt = 0

    print(f"[Part1] : {elves[0]}")

    elves = []
    for i in range(3001330):
        elves.append(i + 1)

    elfCounter = 0
    while len(elves) > 1:
        if len(elves) % 10000 == 0:
            print(len(elves))
        removeElfNo = len(elves) // 2 + elfCounter
        if removeElfNo > len(elves) - 1:
            removeElfNo -= len(elves)
        else:
            elfCounter += 1

        elves.pop(removeElfNo)
        if elfCounter >= len(elves):
            elfCounter = 0

    print(f"[Part2] : {elves[0]}")

